#!/bin/bash
echo 'Initialising image...'
docker build -t /home/$(whoami)/IndividualProject/cyraz-wor:latest .

echo 'Running...'
docker run -d -p 5000:5000
