.. title: test
.. slug: test
.. date: 2020-04-21 11:37:11 UTC+02:00
.. tags:
.. category:
.. link:
.. description:
.. type: text


Write your post here.

Jupyter Notebook metadata
`````````````````````````

Jupyter posts can store meta information inside ``.ipynb`` files by using the ``nikola`` key inside notebook metadata. It can be edited by using *Edit → Edit Notebook Metadata* in Jupyter. Note that values are currently only strings. Sample metadata (Jupyter-specific information omitted):

.. code:: json

    {
        "nikola": {
            "title": "How to make money",
            "slug": "how-to-make-money",
            "date": "2012-09-15 19:52:05 UTC"
        }
    }


YAML metadata
`````````````

YAML metadata should be wrapped by a ``---`` separator (three dashes) and in that case, the usual YAML syntax is used:

.. code:: yaml

   ---
   title: How to make money
   slug: how-to-make-money
   date: 2012-09-15 19:52:05 UTC
   ---

TOML metadata
`````````````

TOML metadata should be wrapped by a "+++" separator (three plus signs) and in that case, the usual TOML syntax is used:

.. code:: yaml

   +++
   title = "How to make money"
   slug =  "how-to-make-money"
   date = "2012-09-15 19:52:05 UTC"
   +++

reST docinfo
````````````

Nikola can extract metadata from reStructuredText docinfo fields and the document itself, too:

.. code:: restructuredtext

    How to make money
    =================

    :slug: how-to-make-money
    :date: 2012-09-15 19:52:05 UTC

To do this, you need  ``USE_REST_DOCINFO_METADATA = True`` in your ``conf.py``,
and Nikola will hide the docinfo fields in the output if you set
``HIDE_REST_DOCINFO = True``.

.. note::
