# Python Base Image from https://hub.docker.com/r/arm32v7/python/
FROM arm32v7/python:3.9-buster

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# use '-u' parameter to NOT buffer python output and see it in docker logs
# must be in ENTRYPOINT (not CMD) to receive Docker SIGINT signal on container stop
ENTRYPOINT ["python", "-u", "connections.py"]
