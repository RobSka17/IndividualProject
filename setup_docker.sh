#!/bin/bash
sudo mv /home/$(whoami)/IndividualProject /home/$(whoami)/cyrazwor
cd /home/$(whoami)/cyrazwor
echo 'Initialising image...'
sudo docker build -t /home/$(whoami)/cyrazwor/cyrazwor .

echo 'Running...'
sudo docker run -d -p 5000:5000 cyrazwor
