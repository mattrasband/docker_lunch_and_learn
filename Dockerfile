FROM python:latest
RUN mkdir -p app
WORKDIR /app

# Note: We moved out our dependencies to be able to gain a layer cache.
# It will only rebuild if we change the file
ADD requirements.txt .
RUN pip install -Ur requirements.txt

ADD . .
CMD python server.py
