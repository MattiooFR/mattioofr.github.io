<!--
.. title: Ma maman géniale
.. slug: ma-maman-geniale
.. date: 2020-03-30 17:29:26 UTC+02:00
.. tags:
.. category: book
.. link:
.. description:
.. type: text
-->

- **Where did I published that ?**

    [Links](https://www.notion.so/3a091934f8e24469a9943df73a09a13d)

**Ressource**

[https://getnikola.com/creating-a-site-not-a-blog-with-nikola.html](https://getnikola.com/creating-a-site-not-a-blog-with-nikola.html)

[https://getnikola.com/getting-started.html](https://getnikola.com/getting-started.html)

[https://jiaweizhuang.github.io/blog/nikola-guide/](https://jiaweizhuang.github.io/blog/nikola-guide/)

[http://www.jaakkoluttinen.fi/blog/how-to-blog-with-jupyter-ipython-notebook-and-nikola/](http://www.jaakkoluttinen.fi/blog/how-to-blog-with-jupyter-ipython-notebook-and-nikola/)

Automatic page load progress bar

[https://github.hubspot.com/pace/docs/welcome/](https://github.hubspot.com/pace/docs/welcome/)

**Themes:**

[https://themes.getnikola.com/v7/mdl/](https://themes.getnikola.com/v7/mdl/)

[https://hackerthemes.com/bootstrap-themes/](https://hackerthemes.com/bootstrap-themes/)

[https://bootswatch.com/](https://bootswatch.com/)

Google group to discuss Nikola : [https://groups.google.com/forum/#!forum/nikola-discuss](https://groups.google.com/forum/#!forum/nikola-discuss)

## 1) Installation

The first step is to have Python 3 installed on your computer, I recommend using virtual environment management, check out this article that talk about it.

Once you have create your virtual environment :

    pip install --upgrade pip setuptools wheel
    pip install --upgrade "Nikola[extras]"

## 2) Create the blog

After installing Nikola, creating your site will be very easy, just use the command `nikola init <directory_name>`. You can add the `--quiet` argument if you want a website built with demo content.

All the configurations are done in a single `[conf.py](http://conf.py)` file, at the root of your blog folder.

You can now build your site and see how it looks like. Use the command `nikola auto` to use a server with automatic rebuilds when changes is detected in your files. Visit [http://128.0.0.1:8000](http://128.0.0.1:8000) to see your site.

## 3) Add a Post

Now if you want to add a post in your blog you should use the command `nikola new_post`(the default use reStructuredText format, add `-f markdown` if like me you prefer to write in markdown). The CLI will ask for the title of your blog post and then create the file in the folder `posts/*.md`.

## 4) Enable Jupyter Notebook file format

Just add *.ipynb as recognizable formats:

    POSTS = (
    	("posts/.rst", "blog", "post.tmpl"),
    	("posts/.md", "blog", "post.tmpl"),
    	("posts/.txt", "blog", "post.tmpl"),
    	("posts/.html", "blog", "post.tmpl"),
    	("posts/.ipynb", "blog", "post.tmpl"), # new line
    )
    PAGES = (
    	("pages/.rst", "", "page.tmpl"),
    	("pages/.md", "", "page.tmpl"),
    	("pages/.txt", "", "page.tmpl"),
    	("pages/.html", "", "page.tmpl"),
    	("pages/.ipynb", "", "page.tmpl"), # new line
    )

You can create a blog post with `nikola new_post -f ipynb` or add your jupyter notebook in your `posts` folder. Don't forget to add and configure these line in the metadata of your jupyter notebook file :

    "nikola": {
       "category": "",
       "date": "2020-03-28 16:27:51 UTC+01:00",
       "description": "",
       "link": "",
       "slug": "jupyter-notebook-test",
       "tags": "",
       "title": "Jupyter Notebook Test",
       "type": "text"
      }

## 5) Using Markdown for your post

Nikola handle markdown files by default. The meta are auto generated when you use `nikola new_post` but I prefer to do it differently. Add the `markdown.extensions.meta` to your `[conf.py](http://conf.py)` file.

    MARKDOWN_EXTENSIONS =
     ['markdown.extensions.fenced_code',
      'markdown.extensions.codehilite',
      'markdown.extensions.extra',
      'markdown.extensions.meta']

Now you can simply add these line on top of your markdown files, in a pelican style, to indicate Nikola all the information it needs to build your post :

    Title: Test post in markdown
    Date: 2020-04-01
    Slug: test-post
    Tags: markdown, test
    Categories: Tutorial

## 6) Creating a landing page

If you want to have a landing page instead of displaying your blog posts directly you need to changed a few settings and understand how it works.

In [conf.py](http://conf.py) :

    INDEX_PATH ="blog"
    .
    .
    .
    POSTS = (
        ("posts/*.html", "posts", "post.tmpl"),
        ("posts/*.ipynb", "posts", "post.tmpl"),
        ("posts/*.md", "posts", "post.tmpl"),
        ("posts/*.rst", "posts", "post.tmpl"),
    )
    PAGES = (
        ("pages/*.html", "", "page.tmpl"), #notice the empty string
        ("pages/*.ipynb", "pages", "page.tmpl"),
        ("pages/*.md", "pages", "page.tmpl"),
        ("pages/*.rst", "pages", "page.tmpl"),
    )

The only file type that I do not want to be output into the pages directory are html files (see commented line above). This is because if I placed "pages" as an output folder, than the index.html that I have written as a landing page would appear in the output pages folder that is not the root directory of the static website generated by Nikola. I want all html files to be generated directly into the output folder that is the root directory of the static website generated by Nikola.

If you place your created index.html file in the output folder, it will not render with elements such as the menubar. Therefore, create a html file using `nikola new_page -f html` so the html file with metadata will be generated. As per the settings ("pages/*.html","","page.tmpl"), all html files in pages will be rendered by Nikola and placed in the root folder (i.e., output).

## 7) **Pages vs Posts**

Nikola has two type for entries on your website, POSTS and PAGES.

**POSTS**

These are your blog posts. POSTS are added to feeds, indexes, tag lists and archives.

**PAGES**

These are generally static pages that may be built when you design your website. Once your design will be done you should not been making many new pages.

For example in PAGES, I have the following bespoke pages:

- [Landing page](https://randlow.github.io/index.html) (html)
- [About me](https://randlow.github.io/about-me) (html)
- [Contact Me](https://randlow.github.io/contact) (html)

## 8) Customizing the navigation bar

Customization of the navigation top bar is done, again, in the `[conf.py](http://conf.py)` file.

    NAVIGATION_LINKS = {
        DEFAULT_LANG: (
            ("/posts/", "Blog"),
            (
                (
                    ("/categories/cat_machinelearning/", "Machine Learning"),
                    ("/categories/cat_trading/", "Tutorial"),
                    ("/categories/cat_books/", "Books"),
                    ("/categories/cat_trading/", "Trading"),
                    ("/archive.html/", "Archived Posts"),
                ),
                "Categories"
            ),
            ("/resume/", "Resume"),
            ("/cheatsheet/", "Cheatsheet"),
            ("/contact/", "Contact"),
        ),

        "fr": (
            ("/posts/", "Blog"),
            (
                (
                    ("/categories/cat_machinelearning/", "Machine Learning"),
                    ("/categories/cat_trading/", "Tutoriel"),
                    ("/categories/cat_books/", "Livres"),
                    ("/categories/cat_trading/", "Trading"),
                    ("/archive.html/", "Articles Archivés"),
                ),
                "Catégories"
            ),
            ("/resume/", "Mon CV"),
            ("/cheatsheet/", "Cheatsheet"),
            ("/contact/", "Contact"),
        ),
    }

This  is an example of how I've done mine, knowing that I have my blog translated to french.

## Files and Listings

This two folders are used to transfer any file or code file to the output folder (your generated website). By default, putting anything in the `files` folder will be available in the root of your website. Anything in `listings` or subfolder will be available in `output/listings`. This last folder allows user to view and download any code file you put in this.

## Date formatting

You can customize how the timestamp are displayed on your blog posts.

    DATE_FORMAT = 'yyyy-MMM-dd'
    DATE_FANCINESS = 2

I like to set it like this to have a more human friendly reading with dates displayed like "3 months ago".

## Categories & Tags

You can use categories and tags to differentiate your blog posts. A post can only belong in one category but it can have multiple tags. Here is the config to set in `[conf.py](http://conf.py)` to enable it:

    CATEGORY_PATH = "categories"
    CATEGORY_PREFIX = "cat_"
    CATEGORY_ALLOW_HIERARCHIES = False
    CATEGORY_OUTPUT_FLAT_HIERARCHY = False
    CATEGORIES_INDEX_PATH = "categories.html"

## Customizing the category landing pages

Instead of the classic "Posts about CATEGORY" landing page title, you can set those by configuring this in `[conf.py](http://conf.py)` :

    CATEGORY_TITLES = {
       DEFAULT_LANG: {
           "machinelearning": "Machine Learning",
           "tutorial": "Tutorials",
           "book": "Books",
           "finance": "Finance & Economy",
       },

       "fr": {
           "machinelearning": "Machine Learning",
           "tutorial": "Tutoriels",
           "book": "Livres",
           "finance": "Finances & Economies",
       }
    }

In the category description you can set actual HTML code :



## Using mailchimp for user to subscribe

Mailchimp allows you to run e-mail campaigns and contact subscribers when you have new content on your site. See [Getting Started with Mailchimp](https://mailchimp.com/help/getting-started-with-mailchimp/) for more detailed instructions.

After you created your account you can create your signup form and get a code that looks like this one. Create a MAILCHIMP_SIGNUP variable in `[conf.py](http://conf.py)` and paste it with """ around it.

    MAILCHIMP_SIGNUP = """
    <!-- Begin Mailchimp Signup Form -->
    <div id="mc_embed_signup">
    <form action="<YOUR MAILCHIMP IDENTIFIER>" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
        <div id="mc_embed_signup_scroll">
    	<label for="mce-EMAIL">Subscribe</label>
    	<input type="email" value="" name="EMAIL" class="email" id="mce-EMAIL" placeholder="email" required>
        <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
        <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_3ffb6593478debd1efe5bf3e7_e432d28210" tabindex="-1" value=""></div>
        <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
        </div>
    </form>
    </div>

    <!--End mc_embed_signup-->
    """

## **16 Indexes as a *list of links* or *list of posts*?**

Nikola allows you to categorize posts in a number of ways such as category, tags, archives, and authors. For each means of categorizing, an associated index page is generated so that viewers can see all available posts (***_PAGES_ARE_INDEXES = True) or links associated to that category (***_PAGES_ARE_INDEXES = False).

You can choose for these indexes to produce a list of the full posts (or [Showing teasers instead of the full post](https://randlow.github.io/posts/python/create-nikola-coding-blog/#showing-teasers-instead-of-the-full-post)) or a list of links to each post. Depending on your needs, you can change any of the following index settings in conf.py to True.

    CATEGORY_PAGES_ARE_INDEXES = False
    TAG_PAGES_ARE_INDEXES = False
    ARCHIVES_ARE_INDEXES = False
    AUTHOR_PAGES_ARE_INDEXES = False

This is what makes Nikola so customizable. For example, since here are less Categories, and you may have more posts under each category, you might want them as a list of links. Alternatively, with Tags there are usually more of them, so less posts under each Tag so you want a list of posts.

## **17 Showing teasers instead of the full post**

The index.tmpl will generate a list of posts associated to the tag/category/year/author. This index can either be the (i) entire post (ii) post with just the teasers. To just show a teaser of the post, set conf.py as follows:

    INDEX_TEASERS = True

In Markdown or html or ipynb, select the end of your teasers with:

    <!-- TEASER_END -->

In reStructuredText, select the end of your teasers with:

    .. TEASER_END

If you are using teasers, the default is a Read more... link to access the full post. To make it more informative, you can have statements such as XX minute read... in conf.py as shown below.

    INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{reading_time} minute read…</a></p>'
    FEED_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'

## Setting your favicon

Pick an icon and store it in the folder '/file/', then edit the [conf.py](http://conf.py) as follows :

    FAVICONS = (
        ("icon", "/brain.png", "128x128"),
    )

## **[19 Deploying the website onto GitHub pages](https://randlow.github.io/posts/python/create-nikola-coding-blog/#id19)**

You will need to have a [GitHub](https://github.com/) account, and enable [GitHub pages](https://pages.github.com/) to deploy your webpage to your GitHub page (i.e., [https://randlow.github.io](https://randlow.github.io/))

By using the nikola github_deploy command, this will create a src branch that will contain your contents (i.e., `*.pynb`, `*.rst`), and a master branch that will contain your html output pages that are viewed by the browser.

    $ nikola github_deploy

Initialize github in your source directory (i.e., github/blog)

    $ git init .
    $ git remote add origin https://github.com/<USER_NAME>/<USER_NAME>.github.io

The conf.py should have the following settings.

    GITHUB_SOURCE_BRANCH = 'src'
    GITHUB_DEPLOY_BRANCH = 'master'
    GITHUB_REMOTE_NAME = 'origin'
    GITHUB_COMMIT_SOURCE = True

Create a .gitignore file with the following entries as a minimum. You may use [gitignore.io](https://www.gitignore.io/) to generate a suitable set of .gitignore entries for your platform by typing in the relevant tags (e.g., linux,`nikola`,jupyternotebooks`).

    cache
    .doit.db
    __pycache__
    output
    ipynb_checkpoints
    */.ipynb_checkpoints/*

## **[20 Archives](https://randlow.github.io/posts/python/create-nikola-coding-blog/#id20)**

Nikola has many options for how you would display your archive of posts. I've kept it pretty simple on my end.

    # Create per-month archives instead of per-year
    CREATE_MONTHLY_ARCHIVE = False
    # Create one large archive instead of per-year
    CREATE_SINGLE_ARCHIVE = False
    # Create year, month, and day archives each with a (long) list of posts
    # (overrides both CREATE_MONTHLY_ARCHIVE and CREATE_SINGLE_ARCHIVE)
    CREATE_FULL_ARCHIVES = False
    # If monthly archives or full archives are created, adds also one archive per day
    CREATE_DAILY_ARCHIVE = False
    # Create previous, up, next navigation links for archives
    CREATE_ARCHIVE_NAVIGATION = False
    ARCHIVE_PATH = "archive"
    ARCHIVE_FILENAME = "archive.html"

## Code color scheme

You can change it in the conf.py, I personally prefer the monokai color scheme :

    CODE_COLOR_SCHEME = 'monokai'

## License

I use the recommended license :

    LICENSE = """
    <a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
    <img alt="Creative Commons License BY-NC-SA"
    style="border-width:0; margin-bottom:12px;"
    src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png"></a>"""

## **[24 Content Footer](https://randlow.github.io/posts/python/create-nikola-coding-blog/#id24)**

You might want to have a specific message (i.e., license, copyright, contact e-mail address) at the footer of every page and this is where to do it. In this case I've added a [Mailchimp](https://mailchimp.com/) link so that readers can subscribe to my page.

    CONTENT_FOOTER = '''
    <center>
    ''' + MAILCHIMP_SIGNUP + '''
    <br>
    Contents &copy; {date} <a href="mailto:{email}">{author}</a> - Powered by         <a href="https://getnikola.com" rel="nofollow">Nikola</a>         {license}'
    </center>
    <br>
    '''

## **[25 Rendering math equations](https://randlow.github.io/posts/python/create-nikola-coding-blog/#id25)**

I have enabled KaTeX because its prettier with the `$...$` syntax as thats more similar to LaTeX.

    USE_KATEX = True
    KATEX_AUTO_RENDER = """
    delimiters: [
        {left: "$$", right: "$$", display: true},
        {left: "\\\\[", right: "\\\\]", display: true},
        {left: "\\\\begin{equation*}", right: "\\\\end{equation*}", display: true},
        {left: "$", right: "$", display: false},
        {left: "\\\\(", right: "\\\\)", display: false}
    ]
    """

## **[26 Showing & copying sources code for posts & pages?](https://randlow.github.io/posts/python/create-nikola-coding-blog/#id26)**

If you would like to enable viewers to be able to show the link of the source of your posts, or copy the source this is easily done. I have disabled these settings for now.

    SHOW_SOURCELINK = False
    COPY_SOURCES = False

## **[28 Implementing external web utilities](https://randlow.github.io/posts/python/create-nikola-coding-blog/#id28)**

### **[28.1 Google search](https://randlow.github.io/posts/python/create-nikola-coding-blog/#id29)**

I've enabled Google search form to search my site.

    SEARCH_FORM = """
     <form method="get" action="https://www.google.com/search" class="form-inline my-2 my-lg-0" role="search">
     <div class="form-group">
     <input type="text" name="q" class="form-control mr-sm-2" placeholder="Search">
     </div>
     <button type="submit" class="btn btn-secondary my-2 my-sm-0">
        <i class="fas fa-search"></i></button>
     </button>
     <input type="hidden" name="sitesearch" value="%s">
     </form>
    """ % SITE_URL

### **[28.2 Disqus (Comments system)](https://randlow.github.io/posts/python/create-nikola-coding-blog/#id30)**

To have a comments system available on your Nikola website, I recommend [Disqus](https://disqus.com/profile/login/). Disqus is easy to setup and works well. Sign up for an account and Add Disqus to site. Follow the instructions and your COMMENT_SYSTEM_ID for Disqus is given by the Website Name that can be found on the Configure Disqus for your site.

    COMMENT_SYSTEM = "disqus"
    COMMENT_SYSTEM_ID = "<YOUR DISQUS WEBSITE NAME>"

Some people have concerns about the fact that [Disqus](https://disqus.com/profile/login/) owns the copyright to your comments, but I'm not bothered.

### **[28.4 Addthis (Social media sharing)](https://randlow.github.io/posts/python/create-nikola-coding-blog/#id32)**

Using [Addthis](https://www.addthis.com/) allows new icons to pop up on your page so that readers can share via a variety of social media platforms. When you sign up and configure what your social media icons look like, you can select Get the Code to obtain the html snippet that looks like the below with your website's unique identifier.

    SOCIAL_BUTTONS_CODE = """
    <!-- Go to www.addthis.com/dashboard to customize your tools -->
    <script type="text/javascript" src="<YOUR ADDTHIS IDENTIFIER>"></script>
    """


### **[28.5 FontAwesome (Fonts & Icons)](https://randlow.github.io/posts/python/create-nikola-coding-blog/#id33)**

I use several icons from [FontAwesome](https://www.fontawesome.com/) on my main landing page. The link to the FontAwesome stylesheeds needed to be added into the pages HEAD tag. Once this is added, you can access all the icons and cool functionality you get with FontAwesome like stacking, rotation, animation, and more.

    EXTRA_HEAD_DATA = """
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.3/css/all.css"
        integrity="sha384-UHRtZLI+pbxtHCWp1t77Bi1L4ZtiqrqD80Kn4Z8NTSRyMA2Fd33n5dQ8lWUE00s/" crossorigin="anonymous">
    """


### **[28.6 Adding Google Analytics & Google AdSense](https://randlow.github.io/posts/python/create-nikola-coding-blog/#id34)**

Google Analytics & Google AdSense can be added to the bottom of <body> to function.

    BODY_END = """
    <!-- Global Site Tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=GA_TRACKING_ID"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', '<YOUR GOOGLE ANALYTICS IDENTIFIER>');
    </script>
    <!-- Google AdSense -->
    <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
    <script>
      (adsbygoogle = window.adsbygoogle || []).push({
        google_ad_client: "<YOUR GOOGLE ADSENSE IDENTIFIER>",
        enable_page_level_ads: true
      });
    </script>
    """

## **[29 Installing plugins](https://randlow.github.io/posts/python/create-nikola-coding-blog/#id35)**

Plugins allow additional functionality for your Nikola website.See [Plugins for Nikola](https://plugins.getnikola.com/) for the full list.

To install plugins, use the following command:

    nikola plugin -i <PLUGIN_NAME>

To remove plugins, use the following command:

    nikola plugin -r <PLUGIN_NAME>

Some interesting plugins that I think are interesting are:

- **medium.** Publish your Nikola posts on Medium.
- **similarity.** Find posts that are similar to the one being read. Requires install of Natural Language Processing packages such as gensim.
- **static_tag_cloud.** Create a nice tag cloud.
- **contentful.** Interface for using a web UI to edit posts and pages.

## **[30 Theme & Template customization](https://randlow.github.io/posts/python/create-nikola-coding-blog/#id36)**

I'm pretty happy with themes available with Nikola (or too lazy to build my own!). However, there are certain tweaks I'd like to make to the webpage and the best way to do this is to customize the templates.

To create a new theme, we can use the following command which will create a new folder in themes called pythonicfinance which is using the mako templating engine and whose parent theme is`bootstrap4`. We don't necessarily want to create a theme from scratch, so we base it off the bootstrap4 theme (or whatever theme you want) and make the adjustments that we want.

    $ nikola theme --new=pythonicfinance --engine=mako --parent=bootstrap4

We can also copy over any templates from the parent theme that we need to make adjusments to by using the following command

    $ nikola theme --copy-template=base.tmpl

If you want to examine all the components of the parent theme (i.e., bootstrap4 in my case), the following command will give you the path to the parent theme for you to explore.

    $ nikola theme -g bootstrap4

The full list of templates is shown below:

    .
    ├── authors.tmpl
    ├── base_helper.tmpl
    ├── base.tmpl
    ├── gallery.tmpl
    ├── index_helper.tmpl
    ├── listing.tmpl
    ├── pagination_helper.tmpl
    ├── post.tmpl
    ├── tags.tmpl
    └── ui_helper.tmpl

In my theme, I wanted to make the nav bar sticky to the top, so that when readers scroll downwards, they can still access the menu bar. To do so, I updated the base.tmpl file as shown below with the command sticky-top.

    <nav class="navbar navbar-expand-md sticky-top mb-4

How to use Interactive Bokeh Plot on Nikola Sites.

[https://jiaweizhuang.github.io/blog/bokeh-in-nikola/](https://jiaweizhuang.github.io/blog/bokeh-in-nikola/)

### Remove .html suffix from archive.html

This is just a small annoyance, but by default, the archive is located in /archive.html. If you want it to be in /archive/, add the following lines to your [conf.py](http://conf.py/):

    ARCHIVE_PATH = "archive"
    ARCHIVE_FILENAME = "index.html"

Remember to also fix the navigation links:

    NAVIGATION_LINKS = {
        DEFAULT_LANG: (
            ("/archive/", "Archive"),
            ("/categories/", "Tags"),
            ("/rss.xml", "RSS feed"),
            ("/about/", "About"),
        ),
    }

### Use KaTeX

In the [conf.py](http://conf.py) change the key `USE_KATEX = True`

### Short blog post teaser in index page

To show only short teasers instead of full posts on index pages:

    INDEX_TEASERS = True

Remember to mark the teasers in your blog posts with <!-- TEASER_END --> in Markdown.

## Enable comment system

Because static sites do not have databases, you need to use a thiry-party comment system as documented on the official doc. The steps are:

1. Sign up for an account on [https://disqus.com/](https://disqus.com/).
2. On Disqus, select "Create a new site" (or visit [https://disqus.com/admin/create/](https://disqus.com/admin/create/)).
3. During configuration, take note on the "Shortname" you use. Other configs are not very important.
4. At "Select a plan", choosing the basic free plan is enough.
5. At "Select Platform", just skip the instructions. No need to insert the "Universal Code" manually, as it is built into Nikola. Keep all default and finish the configuration.

In [`conf.py`](http://conf.py/), add your Disqus shortname:

    COMMENT_SYSTEM = "disqus"
    COMMENT_SYSTEM_ID = "[disqus-shortname]"

Deploy to GitHub and the comment system should be enabled.
