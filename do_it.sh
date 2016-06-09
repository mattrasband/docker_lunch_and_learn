#!/usr/bin/env bash

set -o xtrace
docker build \
    -t docker.nextgearcapital.com/matt.rasband/timeserver:latest \
    -t docker.nextgearcapital.com/matt.rasband/timeserver:dev \
    .

docker push docker.nextgearcapital.com/matt.rasband/timeserver
