FROM python:3.6-alpine

EXPOSE 8000

RUN apk add --no-cache gcc python3-dev musl-dev

ADD . /lab06_ds

WORKDIR /lab06_ds

RUN pip install -r requirements.txt

RUN python lab06_ds/manage.py makemigrations

RUN python lab06_ds/manage.py migrate

CMD [ "python", "django_ec2_project/manage.py", "runserver", "0.0.0.0:8000" ]
