from setuptools import setup

from codecs import open
from os import path

# Get the long description from the README file
long_description = ''
try:
    with open(path.join(path.abspath(path.dirname(__file__)), 'README.rst')) as f:
        long_description = f.read()
except IOError:
    print("could not locate README")
    pass


setup(
    name='ipython-cache',
    version='0.2.5',
    packages=['cache_magic'],
    url='https://github.com/SmartDataInnovationLab/ipython-cache',
    long_description=long_description,
    license='',
    author=u'Bjoern Juergens',
    author_email='juergens@teco.edu',
    description='versatile cache line magic for ipython',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Framework :: IPython',
        'Framework :: Jupyter',
        'Intended Audience :: Science/Research',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Information Analysis'
    ],
    install_requires=[
        'astunparse',
        'IPython',
        'tabulate'
    ],
)
