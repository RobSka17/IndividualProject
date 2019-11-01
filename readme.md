-- INTRO --

Welcome to the readme for the 'Cyraz: War of Realms' card search and deck building app!
This app was developed in Ubuntu 16.04 and is hosted on a Google Cloud virtual instance.
The app comes with the option of manually following the instructions below or using the appropriate intaller.

-- PRE-REQUISITES --

Before you can make use of the app, you'll need to install a few dependencies.
To do this, simply run the following commands in your terminal:
sudo apt-get update
sudo apt-get install -y python3-pip
sudo apt-get install -y python3-venv

-- RUNNING CYRAZ: WAR OF REALMS --

To initiate your download of the application files, run the following in your terminal:
git clone https://github.com/RobSka17/IndividualProject.git
Now, to run the application for the first time, run the following:
cd IndividualProject
. venv/bin/activate
pip3 install -r requirements.txt
python3 run.py
