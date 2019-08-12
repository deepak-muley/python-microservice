sudo apt-get install -y  python3-pip
sudo pip3 install virtualenvwrapper

export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh

mkvirtualenv pythonmicroserviceenv
#deactivate

sudo pip3 install wheel
#sudo pip3 install twine
sudo pip3 install tox
#sudo pip3 install cookiecutter

