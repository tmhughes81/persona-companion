FROM ubuntu

RUN groupadd -g 1000 appuser && \
    useradd -r -u 1000 -g appuser appuser

ENV PYTHONUNBUFFERED=1

RUN apt update && \
	apt install -y python3 python3-pip sudo

RUN pip install django pyyaml django-bootstrap-v5

#USER appuser

WORKDIR /opt
COPY django_project/ /opt/django_project

CMD ["sudo", "/usr/bin/python3", "/opt/django_project/manage.py", "runserver", "0.0.0.0:8000"]
