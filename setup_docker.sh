#!/bin/bash
echo 'Initialising image...'
docker build -t /home/$(whoami)/cyraz-wor/cyraz-wor:latest .

echo 'Running...'
docker run -d -p 5000:5000
