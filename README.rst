=============================
django-ratings-models
=============================

.. image:: https://badge.fury.io/py/django-ratings-models.svg
    :target: https://badge.fury.io/py/django-ratings-models

.. image:: https://requires.io/github/exolever/django-ratings-models/requirements.svg?branch=master
     :target: https://requires.io/github/exolever/django-ratings-models/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://travis-ci.org/exolever/django-ratings-models.svg?branch=master
    :target: https://travis-ci.org/exolever/django-ratings-models

.. image:: https://codecov.io/gh/exolever/django-ratings-models/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/exolever/django-ratings-models

.. image:: https://sonarcloud.io/api/project_badges/measure?project=openexo-django-ratings-models&metric=alert_status
   :target: https://sonarcloud.io/dashboard?id=openexo-django-ratings-models

ratings for your Django models


Quickstart
----------

Install django-ratings-models::

    pip install django-ratings-models

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'ratings',
        ...
    )

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
