

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='cache_magic',
    version='0.1.2',
    description='Adds cache line-magic to ipython',
    long_description=long_description,
    author='Björn Jürgens',
    author_email='juergens@teco.edu',
    license='JSON',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: IPython',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        'astunparse',
        'IPython',
        'datetime',
        'tabulate'
    ],
    keywords='cache magic line-magic ipython',
)
