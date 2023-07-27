#!/bin/bash

image=$1

if [ "$image" == "" ]
then
    image="persona-app"
fi

docker build  -t ${image} .
