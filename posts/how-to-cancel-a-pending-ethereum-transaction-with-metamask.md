<!--
.. title: How to cancel a pending ethereum transaction with MetaMask
.. slug: how-to-cancel-a-pending-ethereum-transaction-with-metamask
.. date: 2020-08-15 12:05:27 UTC+02:00
.. tags: ethereum, metamask, blockchain
.. category: tutorial
.. link:
.. description: Cancel pending ethereum transaction using MetaMask chrome plugin.
.. type: text
.. previewimage: /images/ethereum.jpg
.. medium: yes
.. devto: yes
-->

Having a **pending transaction** can be quite annoying and usually happens when the network is heavy loaded and the fees are sky rocketing. Your transaction may have a **too low gas fee** and miner are just ignoring it to prefer others transaction with higher fees.

This result in you being stuck because until that transaction is resolved you cannot send any other transaction. Annoying right ?

Let's dive right in on how to fix this !

<!-- TEASER_END -->

## Gather all the informations we need

### Prerequisite

This tutorial is about using **MetaMask** to cancel the pending transactions so you need to have it.

If you don't have MetaMask installed on chrome, [here](https://metamask.io/) is the official address to do so.

### Etherscan

The first step is to go on **etherscan** and paste the tx hash of your pending transaction. You can also paste your ethereum address and will be able to find all your pending transactions.

![](/images/cancelethereum/Untitled.png)

Find the oldest pending transaction, click on it and then click on **Click to see More ↓** to get the **Nonce** number of that transaction.

![](/images/cancelethereum/Capture_decran_2020-08-15_a_10.54.48.png)

All the transactions of an ethereum address have a nonce number that increment after each transaction.

![](/images/cancelethereum/Untitled%201.png)

Now the concept behind cancelling a pending transaction is to actually send a new transaction with the same **Nonce** but with a higher fees that the miner will verify and confirm. When this will be done, the previous pending transaction with the same nonce will simply be cancelled and forget by the network because only unique nonce transaction per ETH address can exists.

You should have those informations for going to the next phase :

- Your Ethereum address
- The Nonce of your blocked pending transaction
- MetaMask installed and running with your Ethereum address

## How can I send my own custom transaction

The basic configuration of MetaMask doesn't allow us to use custom Nonce, but you can enable that option in the configuration.

### Enabling the custom gas settings and custom nonce

1. Click on this button

    ![](/images/cancelethereum/Capture_decran_2020-08-15_a_11.03.58.png)

2. The go into the settings

    ![](/images/cancelethereum/Capture_decran_2020-08-15_a_11.05.19.png)

3. Now click on **Advanced**
4. I suggest to enable both **Advanced gas controls** and **Customize Transaction nonce**

### Sending a custom transaction to fix the pending tx

1. Once that's done, quit the configuration and now click on the SEND button.

    ![](/images/cancelethereum/Capture_decran_2020-08-15_a_11.08.22.png)

2. Paste your ETH address, and then add 10 GWEI to the transaction fee gas price to be sure you are above the network average Gas Price so this transaction won't be stuck pending as well. Always verify on [Eth Gas Station](https://ethgasstation.info/) and use a Gas Price above the FAST recommendation. Leave Gas Limit as it is (21000).

    Click on Next when you are done.

    ![](/images/cancelethereum/Capture_decran_2020-08-15_a_11.15.32.png)

3. In this screen you should be able to set your own custom Nonce if you enable it properly in MetaMask config as explained in the beginning of that article. Write down the Nonce of your blocked pending transaction and click on Confirm.

    ![](/images/cancelethereum/Capture_decran_2020-08-15_a_11.17.25.png)

4. MetaMask will ask you to sign your transaction and how will depend on if you are using a Ledger or something else. Once you did sign it, the transaction will be sent and if you were above the FAST Gas Price recommendation from Eth Gas Station website it should be confirmed in less than a minute and your blocked pending transaction should now be cancelled.
5. If you had other pending transaction after that one that are still blocked after this, you will need to repeat the process for each one of them, from the oldest to the newest until you eventually cleared your whole pile of pending transactions.

### How can I prevent that from happening again

Regularly keep an eye on the Eth Gas Station website to know the current average Gas Price, and don't always trust pre configured gas price from MetaMask. If you are doing a transaction that is very important, you can always Edit the Gas Price MetaMask is choosing for you and set it to fast, or even a custom one that you decide.
