#!/bin/bash
docker run -it --mount src=../db,target=/mnt/db,type=bind --mount src=./django_project,target=/mnt/,type=bind persona-app /bin/bash
