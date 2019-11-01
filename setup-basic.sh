#!/bin/bash
echo 'Getting base requirements...'
sudo apt-get update
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-venv

echo 'Renaming directory to cyraz-wor...'
sudo mv /home/$(whoami)/IndividualProject /home/$(whoami)/cyraz-wor
cd /home/$(whoami)/cyraz-wor

echo 'Initialising virtual environment...'
. venv/bin/activate

echo 'Installing additional requirements...'
pip3 install -r requirements.txt

echo 'Running...'
python3 run.py
