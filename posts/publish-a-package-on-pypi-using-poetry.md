<!--
.. title: Publish a package on PyPi using Poetry
.. slug: publish-a-package-on-pypi-using-poetry
.. date: 2020-04-23 21:31:25 UTC+02:00
.. tags: poetry, package
.. category:
.. link:
.. description: Tutorial to publish a package on PyPi using Poetry
.. type: text
.. medium: yes
.. devto: yes
-->

First thing first, you need Poetry if you don't have it already.

Poetry is the new standard for creating and managing virtual environment for your Python project. It is also a Python dependency management tool that is working differently as pip. It uses the new standard `pyproject.toml` decided by the Python Packaging Authority with PEP-518. This file merges all the previous config files that were necessary before, [`setup.py`](http://setup.py/), `requirements.txt`, `setup.cfg`, [`MANIFEST.in`](http://manifest.in/) et `Pipfile`, in one unique file to rule them all ! Ok, enough of Lord of the Ring.

I advice you to follow along with the [documentation](https://python-poetry.org/docs/cli/) of poetry open.
<!-- TEASER_END -->

## Install Poetry

```bash
curl -sSL [https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py](https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py) | python
```

Feel free to look [here](https://python-poetry.org/docs/) for more instructions. Updating Poetry is very easy by the way `poetry update`.

## Create the package you want to publish on PyPi

Poetry has a nice command that can create your project tree at once `poetry new <package_name>`.

```bash
/<package_name>
├── README.rst # I personnaly change it to .md as I prefer writing in Markdown
├── <package_name>
│   └── __init__.py
├── pyproject.toml
└── tests
    ├── __init__.py
    └── test_package_name.py
```

You will need to add things to the generated `pyproject.toml` file, feel free to check the [poetry documentation](https://poetry.eustace.io/docs/pyproject/) to see all the options.

```bash
[tool.poetry]
name = "vspoetry"
version = "0.1.0"
description = "Description of your package"
authors = ["MattiooFR <dugue.mathieu@gmail.com>"]
keywords = ["keyword", "another_keyword"]
readme = "README.md"
license = "MIT"
homepage = "https://github.com/MattiooFR/package_name"
repository = "https://github.com/MattiooFR/package_name"
include = [
    "LICENSE",
]

[tool.poetry.dependencies]
python = "^3.5"

[tool.poetry.dev-dependencies]

[tool.poetry.scripts]
cli_command_name = 'package_name:function'

[build-system]
requires = ["poetry>=0.12"]
build-backend = "poetry.masonry.api"
```

The beginning of the file is pretty straightforward. Lets focus on those three part :

- **[tool.poetry.dependencies]**: This is where you can list all the dependencies that your package needs to work. It's like the old `requirements.txt` file.
You can do it by hand and then call the command `poetry install` to install them all for your package development and working purposes. If you use `poetry add <dependency_name>` (equivalent to the `pip install <dependency_name>`), poetry will add it there for you.
- **[tool.poetry.dev-dependencies]**: If you need development dependencies, that's where they go. Again, you can also install them with `poetry add <dependency_name> --dev (or -D)` and poetry will also put that in the right place in your `pyproject.toml` file.
- **[tool.poetry.scripts]**: This last block is very important if you want your package to have script callable from the terminal.

    ```text
    script_name = '{package_name}:{function_name}'
    ```

By the way, if you still need to have a `requirements.txt` with all the dependencies (if you use Heroku for example), you can easily have it with this command :

```bash
poetry export -f requirements.txt > requirements.txt
```

## Build your package

When your package is ready, simply do `poetry build` to create the package files

```bash
❯ poetry build
Building package_name (0.1.0)
 - Building sdist
 - Built package_name-0.1.0.tar.gz

 - Building wheel
 - Built package_name-0.1.0-py3-none-any.whl
```

You can test your package by doing

```bash
pip install <path_to_package_name-0.1.0-py3-none-any.whl>
```

If everything works, congrats ! Now lets publish it to PyPi so others can use your great package too.

## Publish your package

Before publishing you should first create an account on [PyPi](https://pypi.org/account/register/). You can also register an account on [TestPyPi](https://test.pypi.org/account/register/) if you want publishing on a test repository before trying on the official one.

Your package need to be built, so first run `poetry build` if you haven't done it already.

Then simply run `poetry publish` and your package will be publish on PyPi :

```bash
❯ poetry publish

Publishing vspoetry (0.1.0) to PyPI
Username: Mattioo
Password:
 - Uploading vspoetry-0.1.0-py3-none-any.whl 100%
 - Uploading vspoetry-0.1.0.tar.gz 100%
```

If you need to update your package, simply increment the version in the `pyproject.toml` file and use `poetry publish` (after you build the new package with `poetry build`).

Once you have done that you can then install your package :

```bash
pip install <your_package>

poetry add <your_package> # but lets be honest now you use Poetry so you would do this !
```

Congrats on publishing your package on PyPi and experiencing the simplicity of using a tool like Poetry.

Happy coding !

### End notes

I actually just published my first package, [vspoetry](https://pypi.org/project/vspoetry/), while writing this tutorial. It is a package that add the `vspoetry` script command to my terminal and this simply add the path of the current poetry virtual environment of the project to VScode `settings.json`. This tells to VScode where to grab the project python venv because VScode does not do that automatically yet.
