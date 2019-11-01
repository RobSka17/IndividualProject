#!/bin/bash
echo 'Initialising image...'
sudo mkdir /home/$(whoami)/cyraz-wor
sudo docker build -t /home/$(whoami)/cyraz-wor/cyraz-wor .

echo 'Running...'
sudo docker run -d -p 5000:5000 cyraz-wor
