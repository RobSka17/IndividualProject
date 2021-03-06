#!bin/bash
echo 'Getting base requirements...'
sudo apt-get update
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-venv
echo 'Getting additional requirements info...'
pip3 freeze  > application/requirements.txt
echo $(ls)
echo 'Installing additional requirements...'
sudo pip3 install -r application/requirements.txt
echo 'Exporting for launch...'
export FLASK_APP=run.py FLASK_ENV=production FLASK_RUN_HOST=0.0.0.0 FLASK_RUN_PORT=5000 LC_ALL=C.UTF-8 LANG=C.UTF-8
python -m flask run
