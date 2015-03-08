SECRET_KEY = '&zpihu!t^6rgzs$@-myyw-iwxma3^zx##hd%g9(8pux*2k!+c9'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS = (
    'django_misaka',
    'tests'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware'
)
