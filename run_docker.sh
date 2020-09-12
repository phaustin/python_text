#!/bin/bash -v
export HOST_HUB_HOMEDIRS="/Users/phil/repos/python_text/home_dirs"
#
# Read NETWORK_NAME from .env
#
export $(grep NETWORK_NAME= .env | xargs)
#
# Read HUB_CONTAINER_NAME from .env
#
export $(grep HUB_CONTAINER_NAME= .env | xargs)
docker-compose up
