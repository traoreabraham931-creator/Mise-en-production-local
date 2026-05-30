#!/bin/bash
# deletion of all of the existing containers
docker rm -vf $(docker ps -aq)
# deletion of all of the existing images
docker rmi -f $(docker images -aq)
# creation of the new docker containers
docker build -t stock_predictor .
#Build the container
docker run -d --name stock_predictoon -p 8000:8000 stock_predictor
# http://0.0.0.0:8000/docs









