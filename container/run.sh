#!/bin/bash
if [ "$image" == "" ]
then
    image="persona-app"
fi

docker run -p 127.0.0.1:8000:8000 --mount src=$(pwd)/../db,target=/opt/django_project/db/,type=bind $image
