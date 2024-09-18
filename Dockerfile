# syntax=docker/dockerfile:1

FROM python:3.10-alpine
WORKDIR /flask
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirement.txt requirement.txt
RUN pip install -r requirement.txt
COPY . .
RUN python -m flask --app board init-db
EXPOSE 5000
CMD ["python", "-m", "flask", "--app", "board", "run", "--host=0.0.0.0"]
