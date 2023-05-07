# Django-Misaka

[![Continuous Integration](https://github.com/chiehtu/django-misaka/actions/workflows/tox.yml/badge.svg)](https://github.com/chiehtu/django-misaka/actions)
[![Code Coverage](https://coveralls.io/repos/chiehtu/django-misaka/badge.svg?branch=master)](https://coveralls.io/r/chiehtu/django-misaka?branch=master)
[![Latest Version](https://img.shields.io/pypi/v/django-misaka.svg?style=flat)](https://pypi.python.org/pypi/django-misaka/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/django-misaka.svg?style=flat)](https://pypi.python.org/pypi/django-misaka/)
[![License](https://img.shields.io/pypi/l/django-misaka.svg?style=flat)](https://pypi.python.org/pypi/django-misaka/)

Now this app provide template filter and tag, Misaka API is not yet available.

## Installation

1. Install from PyPI::

    ```bash
    pip install django-misaka
    ```

2. Add ``django_misaka`` to your ``INSTALLED_APPS``::

    ```python
    INSTALLED_APPS = (
        ...
        'django_misaka',
    )
    ```

## Usage

In your template

* Template filter

```html+django
    {% load markdown %}
    ...
    {{ text|markdown|safe }}
```

* Template tag

```html+django
    {% load markdown %}
    ...
    {% markdown %}
        ...
    {% endmarkdown %}
```

## Changelog

See [CHANGELOG](CHANGELOG.md) for more details.
