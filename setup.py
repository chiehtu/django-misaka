import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-misaka',
    version='0.2.1',
    packages=['django_misaka'],
    include_package_data=True,
    install_requires=[
        'houdini.py',
        'misaka',
        'Pygments',
    ],
    license='MIT',
    description=('A Django template tag for rendering '
                 'Markdown (by Misaka Markdown parser).'),
    long_description=README,
    url='http://github.com/chiehtu/django-misaka/',
    author='Chieh Tu',
    author_email='me@chiehtu.net',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
