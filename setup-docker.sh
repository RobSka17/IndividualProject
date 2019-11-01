#!/bin/bash
echo 'Renaming directory to cyraz-wor...'
sudo mv /home/$(whoami)/IndividualProject /home/$(whoami)/cyraz-wor
cd /home/$(whoami)/cyraz-wor
echo 'Initialising image...'
sudo docker build -t cyraz-wor .

echo 'Running...'
sudo docker run -d --name cyraz-wor -p 5000:5000 cyraz-wor
