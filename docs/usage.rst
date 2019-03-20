=====
Usage
=====

To use django-ratings in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'ratings.apps.RatingsConfig',
        ...
    )

Add django-ratings's URL patterns:

.. code-block:: python

    from ratings import urls as ratings_urls


    urlpatterns = [
        ...
        url(r'^', include(ratings_urls)),
        ...
    ]
