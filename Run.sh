#!/bin/sh
#
docker run -d --rm -p 8080:8080 --name sensor sample_temperature
#docker run -d --rm --privileged --network sensor-network --name sensor sample_temperature
