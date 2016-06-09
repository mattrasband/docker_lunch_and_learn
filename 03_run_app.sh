#!/usr/bin/env bash

set -o xtrace
docker run --rm -it -p 8080:8080 -v "${PWD}":/app python:latest python /app/echo_server.py
