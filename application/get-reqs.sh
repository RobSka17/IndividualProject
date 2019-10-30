#!/bin/bash
echo 'Getting base requirements...'
sudo apt-get update
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-venv
echo 'Getting additional requirements info...'
pip3 freeze --local | grep -v ./ >> requirements.txt
