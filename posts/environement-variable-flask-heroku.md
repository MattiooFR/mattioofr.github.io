<!--
.. title: Using environement variables in a Flask + Heroku project
.. slug: environement-variable-flask-heroku
.. date: 2020-04-19 15:43:36 UTC+02:00
.. tags: flask, heroku
.. category:
.. link:
.. description: Quick tutorial to understand good practices on using environment variables.
.. type: text
-->

Using environment variables is fundamental in a project. This is how you tell your app if you are running in `production` or `locally` for example. This is where you also store more sensible information like `SECRET_KEY` or API credentials. Storing those directly in your web app code can be easy at first, but it is not safe when you will push your code in production, so taking good habits from the beginning is a good idea.

Before jumping in the topic of configuring environment variables, I will first make you set up and deploy a basic app.

<!-- TEASER_END -->

## Flask

In this project I use Flask. Create a folder for your app and a new virtual environment (check out [poetry](https://github.com/python-poetry/poetry) if you don't know what it is). Once your virtual environment is running, we need to install a few dependencies first :

```bash
# if you use poetry as virtual environment manager
# use the command 'poetry add' instead of 'pip install'

pip install flask gunicorn
```

Flask is the web server running with python, and Gunicorn is what will basically run our web server on Heroku when we will deploy our app.

Lets first set up a basic app and create a file `[app.py](http://app.py)` in your folder :

```python
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    greeting = "Hello"
    try:
        excited = os.environ['EXCITED']
        greeting = greeting + "!!!!!"
    except:
        pass

    return render_template("index.html", greeting=greeting)
```

As you see we will render an `index.html` so create that file too inside a `templates` folder and paste this code inside :

```html
<!doctype html>
<html>
    <head>
        <title>My App</title>
    </head>

    <body>
        {{ greeting }}
    </body>
</html>
```

Before running the web app locally we need to set two variable in your terminal so Flask knows what to do exactly :

```bash
export FLASK_ENV=development
export FLASK_APP=app.py
export EXCITED=True
```

Lets run our app locally with `flask run` . As you can see we are greeted like expected, with all the '!!!!', but I had to export the variable in my terminal. Every time you close your terminal you need to do that again. Not very efficient.

## Heroku

Now if we want to deploy our app on Heroku we need to do a few things.

1. Create a `Procfile` at the root of your folder. Paste this code inside :

    ```bash
    web: gunicorn app:app
    ```

2. We need to export all the python dependencies in a `requirements.txt` file :

    ```bash
    pip freeze > requirements.txt

    # if you use poetry you can do as following
    poetry export -f requirements.txt > requirements.txt
    ```

3. Install Heroku CLI on your machine and then login on your Heroku account ([here to register](https://signup.heroku.com/)):

    ```bash
    # if you are on mac and use homebrew
    brew tap heroku/brew && brew install heroku

    # you can also use npm
    npm install -g heroku
    ```

4. Once Heroku is available on your terminal, we can create your Heroku App :

    ```bash
    heroku create <name_of_your_app>
    ```

    Now if you check your Heroku Dashboard in the browser, you'll see an application with that name. But it doesn't have our code or anything yet - it's completely empty. Let's get our code up there.

5. The next step is initializing git in your repository, and add the Heroku remote in your git repository :

    ```bash
    git init
    heroku git:remote -a <name_of_your_app>
    ```

6. Now before pushing our app on Heroku, we need to set that `EXCITED` variable to true. You can do that on the web interface of Heroku, or using the CLI with :

    ```bash
    heroku config:set EXCITED=True
    ```

7. To push our web app to Heroku we can simply do :

    ```bash
    git add .
    git commit -m"deploying app on heroku"
    git push heroku master
    ```

Now if you look at [https://name_of_your_app.heroku.com](https://name_of_your_app.heroku.com) you should have a nice excited greeting message : `Hello !!!!`

## Environment Variable

Alright, thank you Mathieu, but how is that suppose to teach us how to manage environment variable ?

Well, now that you are set up properly, let me introduce the `.env`  and `.flaskenv` files. By convention, the `.flaskenv` is where you store your variables related to your flask configuration, such as the type of environment, or the files that contains your flask app. For this example we will write those lines inside this file :

```txt
#.flaskenv file

FLASK_APP=app.py
FLASK_ENV=development
```

Now the `.env` file contains the sensible variable information that your app needs to run. This file stay locally and you must include it in your `.gitignore` to avoid sharing sensible informations. For the purpose of this tutorial we will just include one variable :

```txt
#.env file

EXCITED=True
```

Your folder structure should look something like this :

```txt
.
├── templates
    └── index.html
├── .env
├── .flaskenv
├── .gitignore
├── Procfile
├── app.py
└── requirements.txt
```

Now we have two different use case possible. If you want to use flask to run your app locally you need to install one more dependencies

```bash
pip install python-dotenv

# with poetry use
poetry add python-dotenv
```

You don't need to do anything else, thanks to this new package, flask will automatically detect your two new files and will load their variables in the app context.

If instead of using flask to run your app locally you prefer to use `heroku local web` then you don't need to install `python-dotenv`, Heroku will detect the `.env` file by itself.

## Conclusion

We saw how to implement a behavior that allows us to protect our sensible information by putting them in external files that wont be pushed to a public git repository. In the same time our app will work seamlessly when deployed on Heroku, if you set up the same variables in your `.env` files on the config of your Heroku app (with the web interface or the CLI).

You can find all the code of this tutorial [here](https://github.com/MattiooFR/Tutorials/tree/master/FlaskHerokuEnv).
