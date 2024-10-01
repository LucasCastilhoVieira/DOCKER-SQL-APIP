python3 -m venv venv;
. venv/bin/activate;
pre-commit install;
apt-get update;
apt-get install python-pip
pip3 install -r requirements.txt