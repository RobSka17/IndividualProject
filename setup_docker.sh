#!/bin/bash
sudo mv /home/$(whoami)/IndividualProject /home/$(whoami)/cyraz-wor
echo 'Initialising image...'
sudo docker build -t /home/$(whoami)/cyraz-wor/cyraz-wor:latest .

echo 'Running...'
sudo docker run -d -p 5000:5000 cyraz-wor
