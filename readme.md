-- INTRO --

Welcome to the readme for the 'Cyraz: War of Realms' card search and deck building app!
This app was developed in Ubuntu 16.04 in preparation to be hosted on a Google Cloud virtual instance.
The app comes with the option of manually following the instructions below or using the
setup file associated with your desired setup method.

-- PRE-REQUISITES --

Before you can make use of the app, you'll need to install a few dependencies.
To do this, simply run the following commands in your terminal:

sudo apt-get update

sudo apt-get install -y python3-pip

sudo apt-get install -y python3-venv

-- RUNNING CYRAZ: WAR OF REALMS --

To initiate your download of the application files, run the following in your terminal:

git clone https://github.com/RobSka17/IndividualProject.git

Whichever setup option you select from the options below, the application will run  on local host, on port 5000.

**Basic Setup:**

To run the application in its basic testing form, run the following:

sudo mv /home/$(whoami)/IndividualProject /home/$(whoami)/cyraz-wor

cd /home/$(whoami)/cyraz-wor

. venv/bin/activate

pip3 install -r requirements.txt

python3 run.py

**Docker Setup:**

To run the application as a Docker container application, run the following:

sudo mv /home/$(whoami)/IndividualProject /home/$(whoami)/cyraz-wor

cd /home/$(whoami)/cyraz-wor

sudo docker build -t cyraz-wor .

sudo docker run -d -p 5000:5000 cyraz-wor

Your download will also include a Jenkinsfile which can be used to run the container
through a Jenkins Pipeline. 
