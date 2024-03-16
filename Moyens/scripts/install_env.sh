#!/bin/bash

sudo apt update

# python part
sudo apt install python3-venv libdbus-glib-1-dev
pip install secretstorage dbus-python

python3 -venv venvOnche
pip install -r ../../../requirements.txt