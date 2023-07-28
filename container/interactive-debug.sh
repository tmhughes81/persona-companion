#!/bin/bash
docker run -it --mount src=./django_project,target=/mnt/,type=bind persona-app /bin/bash
