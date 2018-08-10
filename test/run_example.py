#!/usr/bin/env python3

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import CellExecutionError

import os
import shutil

notebook_filename = "example.ipynb"

test_base_dir = "test"
run_path =  os.path.join(test_base_dir, "result")
notebook_filename_out = os.path.join(run_path, "example.out.ipynb")

if os.path.exists(run_path):
    shutil.rmtree(run_path)
os.makedirs(run_path)

with open(notebook_filename) as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

try:
    out = ep.preprocess(nb, {'metadata': {'path': run_path}})
except CellExecutionError:
    out = None
    msg = 'Error executing the notebook "%s".\n\n' % notebook_filename
    msg += 'See notebook "%s" for the traceback.' % notebook_filename_out
    print(msg)
    raise
finally:
    with open(notebook_filename_out, mode='wt') as f:
        nbformat.write(nb, f)
