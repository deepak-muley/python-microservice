
source ./venv3/bin/activate
python3 setup.py sdist
python3 setup.py bdist_wheel
#python3 setup.py develop 
#or
#pip install -e .
ls dist/ 