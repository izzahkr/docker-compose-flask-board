FROM python:3.10-slim
WORKDIR /flask
RUN apt-get update && apt-get install -y gcc python3-dev
COPY requirement.txt requirement.txt
RUN pip install -r requirement.txt
EXPOSE 5000
COPY . .
CMD ["python", "-m", "flask", "--app", "board", "run", "--host=0.0.0.0", "--debug"]
