#!/bin/sh

# fail on error and report it, debug all lines
set -eu

# make sure that they have sudo
sudo -n true
test $? -eq 0 || exit 1 "you should have sudo privilege to run this script"

# Setup and activate the virtual environment to run the python code in
python3 -m venv venv
. venv/bin/activate
echo The virtual environment is here: $VIRTUAL_ENV

# install the required libraries
pip install -r requirements.txt

# test the installation
python3 src/main.py

# close installer
echo Installation complete.