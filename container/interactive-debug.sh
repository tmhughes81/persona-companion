#!/bin/bash
docker run -it --mount src="$(pwd)/../django/",target=/test_container,type=bind persona-app /bin/bash
