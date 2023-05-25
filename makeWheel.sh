#!/usr/bin/bash
python -m pip install wheel
python -m pip install --upgrade pip
python -m pip install check-wheel-contents
python setup.py bdist_wheel
check-wheel-contents ./dist
