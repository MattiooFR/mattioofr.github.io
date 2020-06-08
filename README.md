# This folder contains the source used to generate a static site using Nikola.

Installation and documentation at https://getnikola.com/

* Configuration file for the site is `conf.py`.

* To build the site:

    ``` bash
    nikola build
    ```

* To see it:

    ``` bash
    nikola auto
    ```

* To check all available commands:

    ``` bash
    nikola help
    ```

* Template for the post metadatas:

    ``` md
    .. hidetitle: true
    .. devto: yes
    .. medium: yes
    .. previewimage: /images/image.png <!-- uri to image to display in link preview-->
    .. link: url <!-- url to original source for content-->
    .. has_math: true <!-- for rendering katex -->
    ```

* Using the jupyter_shortcode plugin:

    ``` txt
    {{% jupyter toto.ipynb %}}
    ```

* Placing the ipynb file in the listings folder.

* Place the end of the teaser with :

    ```txt
    <!-- TEASER_END -->
    ```

* Create footnote :

    ```txt
    Text[^lorem] (note) blablabla

    [^lorem] (footnote)
    ```

* This ~~is deleted text.~~
    ``` md
    This ~~is deleted text.~~
    ```

* Shortcut link

    ``` md
    See [my website].

    [my website]: http://foo.bar.baz
    ```