Django-Misaka
-------------

.. image:: https://travis-ci.org/chiehtu/django-misaka.svg?branch=master
    :target: https://travis-ci.org/chiehtu/django-misaka

.. image:: https://coveralls.io/repos/chiehtu/django-misaka/badge.svg?branch=master
    :target: https://coveralls.io/r/chiehtu/django-misaka?branch=master

.. image:: https://pypip.in/version/django-misaka/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/django-misaka/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/django-misaka/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/django-misaka/
    :alt: Supported Python versions

.. image:: https://pypip.in/license/django-misaka/badge.svg?style=flat
    :target: https://pypi.python.org/pypi/django-misaka/
    :alt: License

Now this app provide template filter and tag, Misaka API is not yet available.

Installation
------------

1) Install from PyPI::

    pip install django-misaka

2) Add ``django_misaka`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'django_misaka',
    )

Usage
-----

In your template

- Template filter::

    {% load markdown %}
    ...
    {{ text|markdown|safe }}

- Template tag::

    {% load markdown %}
    ...
    {% markdown %}
        ...
    {% endmarkdown %}

Change log
----------
v0.2.0
^^^^^^
- Add template tag.
- Function ``markdown`` was renamed ``markdown_filter``.
- Update information for author (setup.py).

v0.1.0
^^^^^^
- First version, it's only provides template filter.
