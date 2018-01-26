

# cache magic

This package adds `%cache` line-magic to ipython kernels in jupyter notebooks.

## Quickstart

* The pip-package is called `ipython-cache`
* The python module is called `cache_magic`
* The magic is called `%cache`

So you can run the magic by entering this into an ipython-cell:

    !pip install ipython-cache
    import cache_magic
    %cache a = 1+1
    %cache

## installation

### install directly from notebook

1. open jupyter notebook
2. create new cell
3. enter `!pip install cache-magic`
4. execute

### install into conda-environment

    conda create -n test
    source activate test
    conda install -c juergens ipython-cache
    jupyter notebook

## usage

Activate the magic by loading the module like any other module. Write into a cell `import cache_magic` and excecute it.

When you want to apply the magic to a line, just prepend the line with `%cache`

### example

    %cache myVar = someSlowCalculation(some, "parameters")

This will calculate  `someSlowCalculation(some, "parameters")` once. And in subsequent calls it restores myVar from storage.

The magic turns this example into something like this (if there was no ipython-kernel and no versioning):  

    try:
      with open("myVar.txt", 'rb') as fp:
        myVar = pickle.loads(fp.read())
    except:
      myVar = someSlowCalculation(some, "parameters")
      with open("myVar.txt", 'wb') as fp:
        pickle.dump(myVar, fp)

### general form

    %cache <variable> = <expression>

**Variable**: This Variable's value will be fetched from cache.

**Expression**: This will only be excecuted once and the result will be stored to disk.

### full form

    %cache [--version <version>] [--reset] [--debug] variable [= <expression>]

**-v or --version**: either a variable name or an integer. Whenever this changes, a new value is calculated (instead of returning an old value from the cache).

if version is '\*' or omitted, the hashed expression is used as version, so whenever the expression changes, a new value is cached.

**-r or --reset**: delete the cached value for this variable. Forces recalculation, if `<expression>` is present

**-d or --debug**: additional logging

### show cache

    %cache

shows all variables in cache as html-table

### full reset

    %cache -r
    %cache --reset

deletes all cached values for all variables

## where is the cache stored?

In the directory where the kernel was started (usually where the notebook is located)  in a subfolder called `.cache_magic`


# developer Notes

## push to pypi

prepare environment:

    gedit ~/.pypirc
    chmod 600 ~/.pypirc
    sudo apt install pandoc

upload changes to test and production:

    pandoc -o README.rst README.md
    restview --pypi-strict README.rst
    # update version in setup.py
    rm -r dist
    python setup.py sdist
    twine upload dist/* -r testpypi
    firefox https://testpypi.python.org/pypi/ipython-cache
    twine upload dist/*

test install from testpypi

    pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple ipython_cache --no-cache-dir --user

test installation

    sudo pip install ipython_cache --no-cache-dir --user


## editable import

Install into environment with `-e`:

    !pip install -e .

reload after each change:

    import cache_magic
    from imp import reload
    reload(cache_magic)

Alternatively (if you don't want to install python, jupyter & co), you can use the docker-compose.yml for development:

    cd ipython-cache
    docker-compose up


## create Conda Packet

requires the bash with latest anaconda on path

    bash
    mkdir test && cd test
    conda skeleton pypi ipython-cache
    conda-build ipython-cache -c conda-forge
    anaconda upload /home/juergens/anaconda3/conda-bld/linux-64/ipython-cache-*

## running tests

    bash
    conda remove --name test --all
    conda env create -f test/environment.yml
    source activate test
    conda remove ipython-cache
    pip uninstall ipython_cache
    pip install -e .
    ./test/run_example.py

If there is any error, it will be printed to stderr and the script fails.

the output can be found in "test/temp".
