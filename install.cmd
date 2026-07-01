@echo off
pip install wheel setuptools build
python -m build
pip install dist/*.whl
pip install .
python setup.py install
cls
pip list | findstr choice-functions
pause