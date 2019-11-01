echo 'Getting base requirements...'
sudo apt-get update
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-venv

echo 'Downloading program files...'
git clone https://github.com/RobSka17/IndividualProject.git

echo 'Initialising virtual environment...'
cd IndividualProject 
. venv/bin/activate

echo 'Installing additional requirements...'
pip3 install -r requirements.txt

echo 'Running...'
python3 run.py
