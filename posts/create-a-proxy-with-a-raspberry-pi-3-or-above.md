<!--
.. title: Create a proxy with a Raspberry Pi 3 (or above)
.. slug: create-a-proxy-with-a-raspberry-pi-3-or-above
.. date: 2020-08-27 11:12:16 UTC+02:00
.. tags: raspberry-pi
.. category: tutorial
.. link:
.. description: Tutorial on how to make your own personal home proxy with a Raspberry Pi 3.
.. type: text
.. previewimage: /images/raspberry-pi.jpg
-->

If you need to use a proxy that has the same IP address as your home, here is a tutorial on how to do it.

### Install and configure your Raspberry Pi OS

Install and configure a raspberry pi without a mouse nor a keyboard :

1. Download the last version of raspbian lite [here](https://www.raspberrypi.org/downloads/raspberry-pi-os/) and download [Etcher](https://www.balena.io/etcher/) which we will use to flash the disk image on the SD card.
2. Start Elena, select the Raspbian Lite imake disk, select the target which is the SD card you use for your raspberry pi and click on Flash!.

While the image disk is getting installed, we will create the file that contains the wifi information so the raspberry can connect to it automatically. Open a text note and paste this inside :

<!-- TEASER_END -->

```txt
ctrl_interface=/run/wpa_supplicant
update_config=1
country=FR

network={
	ssid="internet_box_name"
	scan_ssid=1
	psk="password"
}
```

Replace `internet_box_name` and `password` by your home internet box settings and save that file under`wpa_supplicant.conf`

Then we will create an empty file which name is simply `ssh`. This file will tell the raspberry that you want to enable the SSH connection which is usually set off by default. With that settings on we will be able to connect to the raspberry pi through the network using another computer.

Place both files that you just created in the BOOT folder of the SD card you just flashed.

Congratulation ! Now you can eject the SD card and insert it in your raspberry pi.

If everything worked out, when you switch on your Raspberry Pi you should see it in the list of the device connected to your home internet network by checking your router.

Now the next step is to connect to your Raspberry Pi with SSH. Launch a terminal and if you are on mac type this command :

`ssh pi@local_ip_of_your_raspberry`

It will ask for a password, type  `raspberry`

To avoid that IP to change, we will set a static IP to your raspberry. You need to modify the file `dhcpd.conf` located in the folder `/etc/`.

Once you have opened the file, go to the last line and add this content

```bash
interface eth0
static ip_address=192.168.1.100/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1

interface wlan0
static ip_address=192.168.1.100/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1
```

Here, the `eth0` correspond to a internet cable connection, and `wlan0` to a internet wifi connection. Up to you to choose which one you will use.

Static ip_address indicate the IP that your Raspberry Pi will have when it switch on. usually the IP is of the type `192.168.1.x`, replace the x by an available slot on your network. If your box is on a different IP address then modify static router et static domain_name_servers accordingly.

Save the file and exit.

### Setting up the raspberry pi

1) Update the raspberry pi

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
```

2) Install terminal editor Joe

```bash
sudo apt-get install joe
```

3) Install the following

```bash
sudo apt-get -y install fail2ban software-properties-common
sudo apt-get install build-essential libevent-dev libssl-dev
cd /etc
sudo wget https://github.com/z3APA3A/3proxy/archive/0.8.12.tar.gz
sudo tar zxvf 0.8.12.tar.gz
sudo mv 3proxy-0.8.12 3proxy
cd 3proxy
```

4) Edit the file proxy.h

```bash
sudo joe src/proxy.h
```

And add the line following line above the other lines starting with #DEFINE

```bash
#define ANONYMOUS 1
```

5) Compile and install the software

```bash
sudo make -f Makefile.Linux
sudo make -f Makefile.Linux install
```

6) Download 3proxy.cfg

```bash
sudo wget https://gettraffic.pro/docs/3proxy.cfg
```

7) Edit the 3proxy.cfg with Joe

```bash
sudo joe 3proxy.cfg
```

8) Change those lines

```bash
users root:CL:passwd
...
allow root
```

To any username you prefer instead of `root` and change the `passwd` to a strong password. If you changed root to a different username don't forget to change `allow root` to `allow` and whatever username you decided. Save that file when you are finished

9) Change file permission

```bash
sudo chmod 700 3proxy.cfg
```

10) Download the script file

```bash
cd /etc/3proxy/scripts/rc.d/
sudo mv proxy.sh saved-proxy.sh
sudo wget https://gettraffic.pro/docs/proxy.sh
```

11) Start the proxy server

```bash
sudo sh /etc/3proxy/scripts/rc.d/proxy.sh start
```

It should give the output “Starting 3Proxy”. If it doesn’t then there is a problem somewhere in your config files.

12) Add it to the autorun so after reboot it will start again

```bash
sudo joe /etc/rc.local
```

And add line :

```bash
sh /etc/3proxy/scripts/rc.d/proxy.sh start
```

This line has to be added above the line `exit 0`.

The best way to check if everything is alright is by doing a full reboot of your Raspberry and checking if everything still works after the reboot :

```bash
sudo shutdown -r now
```

### Access your Raspberry Pi with SSH outside your home local network

You will need to add the fixed IP you choose for your Raspberry Pi in your internet box router settings. Add this IP address in the DHCP settings (the aim of this tutorial is not to each how to do that so look ressources on google).

Now edit your NAT/PAT settings to redirect the port 22 (SSH) and 3129 (your proxy) to the fixed IP address you just set up in the DHCP.

Now to access your home internet network from outside, you need a way to now its public IP address which might change over time. We will use a very good services to achieve that is called no-ip.

1. Register on [https://www.noip.com/](https://www.noip.com/)
2. Create a hostname like « myraspberrypiproxy.ddns.net »
3. Install the DUC on your raspberry pi which will automatically update the public IP no-ip will redirect the hostname to :

```bash
cd /usr/local/src/
sudo wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz
sudo tar xf noip-duc-linux.tar.gz
cd noip-2.1.9-1
sudo make install
```

4. Then a little bit of configuration

```bash
sudo cp /usr/local/src/noip-2.1.9-1/debian.noip2.sh /etc/init.d/noip2.sh
sudo joe /etc/init.d/noip2.sh
```

5. And add the following code abose this line `DAEMON=/usr/local/bin/noip2`:

```bash
#!/bin/sh
#
### BEGIN INIT INFO
# Provides:          noip2.sh
# Required-Start:    $remote_fs $local_fs
# Required-Stop:     $remote_fs $local_fs
# Should-Start:
# Should-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Dynamic IP client updater
# Description:
### END INIT INFO
```

Now the client can be started, stopped or restarted manually

```bash
sudo /etc/init.d/noip2.sh <start|stop|restart>
    ```

6. Change files read write properties :

```bash
sudo chown root.root /etc/init.d/noip2.sh
sudo chmod +x /etc/init.d/noip2.sh
```

7. Start the server

```bash
sudo /etc/init.d/noip2.sh start
```

8. To allow starting the service automatically at startup, run the following command:

```bash
sudo update-rc.d noip2.sh defaults
```

9. Then try sudo reboot to see if service start by itself

To check if there is a running instance use this command :

```bash
sudo noip2 -S
```

Finish ! Now you should be able to connect to your proxy with the hostname address you used in no-ip and the port 3129 like this 'myraspberrypiproxy.ddns.net:3129'. The authorized username and password to connect to the proxy are the one you decided previously in the step 8 of configuring the proxy.

### Useful Commands

- If you need to reconfigure the DUC file from no-ip use that command :
`sudo /usr/local/bin/noip2 -C`
- Connect to the raspberry pi by SSH with Terminal (Mac) :
`ssh pi@ip`
Then yes, and type password
- Check if there is a no-ip instance running
`sudo noip2 -S`
- Check if proxy is running
`ps -A`
