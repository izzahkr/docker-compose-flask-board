# syntax=docker/dockerfile:1
<<<<<<< HEAD

FROM python:3.10-alpine
WORKDIR /flask
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirement.txt requirement.txt
RUN pip install -r requirement.txt
COPY . .
RUN python -m flask --app board init-db
EXPOSE 5000
CMD ["python", "-m", "flask", "--app", "board", "run", "--host=0.0.0.0"]
=======
FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
>>>>>>> dev
