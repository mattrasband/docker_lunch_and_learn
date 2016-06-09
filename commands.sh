#!/usr/bin/env bash

# brew cask install dockertoolbox
docker-machine create --driver virtualbox ngc
docker-machine ls
eval "$(docker-machine env default)"
docker-machine ls
