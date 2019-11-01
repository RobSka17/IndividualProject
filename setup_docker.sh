#!/bin/bash
echo 'Initialising image...'
sudo docker build -t /home/$(whoami)/cyraz-wor/cyraz-wor:latest .

echo 'Running...'
sudo docker run -d -p 5000:5000 cyraz-wor
