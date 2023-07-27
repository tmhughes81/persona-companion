#!/bin/bash

if [ "$image" == "" ]
then
    image="persona-app"
fi


docker build  -t ${image} .
