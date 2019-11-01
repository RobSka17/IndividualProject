echo 'Initialising image...'
user = $(whoami)
path = /home/$(user)/IndividualProject/cyraz-wor:latest
docker build -t $(path) .

echo 'Running...'
docker run -d -p 5000:5000
