FROM ubuntu

ENV PYTHONUNBUFFERED=1

RUN apt update && \
	apt install -y python3 python3-pip

RUN pip install django

WORKDIR /opt
COPY django_project/ /opt/django_project

CMD ["/usr/bin/python3", "/opt/django_project/manage.py", "runserver", "0.0.0.0:8000"]
