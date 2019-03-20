=============================
django-ratings
=============================

.. image:: https://badge.fury.io/py/ratings.svg
    :target: https://badge.fury.io/py/ratings

.. image:: https://travis-ci.org/marfyl/ratings.svg?branch=master
    :target: https://travis-ci.org/marfyl/ratings

.. image:: https://codecov.io/gh/marfyl/ratings/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/marfyl/ratings

ratings for your Django models

Documentation
-------------

The full documentation is at https://ratings.readthedocs.io.

Quickstart
----------

Install django-ratings::

    pip install django-ratings-models

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'ratings.apps.RatingsConfig',
        ...
    )

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
