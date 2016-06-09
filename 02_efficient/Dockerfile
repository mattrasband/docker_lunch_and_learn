FROM python:latest

RUN mkdir -p app
WORKDIR /app

ADD requirements.txt .
RUN pip install -Ur requirements.txt

ADD . .
CMD python server.py
