# Notice this is the same image as earlier, so we have all the layers
# However each instruction in the file will create an entirely new layer.
FROM python:latest

RUN mkdir -p app
WORKDIR /app

# Good images should be entirely encapsulated, so you cannot
# mount volumes in the dockerfile - we literally copy the
# sources over.
ADD . .

# Just installing my app's dependencies - same as `npm install`
RUN pip install -Ur requirements.txt

EXPOSE 8080

# This isn't actually run during the build, instead it is
# the "entry point" when the container is started.
CMD python server.py
