#!/bin/bash
if [ "$image" == "" ]
then
    image="persona-app"
fi

docker run -p 127.0.0.1:8000:8000 --mount src=$LOCAL_DB_PATH,target=/opt/django-project/db/,type=bind $image
