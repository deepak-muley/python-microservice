#!/bin/bash -e

export PYTHONPATH=$PYTHONPATH:$(pwd)
#python3 test/test_httpbinrestclient.py
python3 -m unittest discover -s ./test