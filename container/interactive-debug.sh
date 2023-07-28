#!/bin/bash
docker run -it --mount src=$(pwd)/../db,target=/opt/django_project/db/,type=bind --mount src=./django_project,target=/mnt/,type=bind persona-app /bin/bash
