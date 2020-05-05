# This folder contains the source used to generate a static site using Nikola.

Installation and documentation at https://getnikola.com/

Configuration file for the site is `conf.py`.

To build the site:

``` bash
nikola build
```

To see it:

``` bash
nikola auto
```

To check all available commands:

``` bash
nikola help
```

Template for the post metadatas:

``` md
.. hidetitle: true
.. devto: yes
.. medium: yes
.. link: url <!-- url to original source for content-->
```

Using the jupyter_shortcode plugin:

{{% jupyter toto.ipynb %}}

Placing the ipynb file in the listings folder.
