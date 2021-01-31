# # first stage
# FROM python:3.8 AS builder
# COPY requirements.txt .

# # install dependencies to the local user directory (eg. /root/.local)
# RUN pip install --user -r requirements.txt

# # second unnamed stage
# FROM python:3.8-slim
# WORKDIR /code

# # copy only the dependencies installation from the 1st stage image
# COPY --from=builder /root/.local/bin /root/.local
# COPY ./src .

# # update PATH environment variable
# ENV PATH=/root/.local:$PATH

# CMD [ "python", "./server.py" ]

# # set base image (host OS)
# FROM python:3.8

# # set the working directory in the container
# WORKDIR /code

# # copy the dependencies file to the working directory
# COPY requirements.txt .

# # install dependencies
# RUN pip install -r requirements.txt

# # copy the content of the local src directory to the working directory
# COPY src/ .

# # command to run on container start
# CMD [ "python", "./server.py" ]

FROM python:3.8
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
# ENV FLASK_APP server.py
# CMD flask run --host=0.0.0.0

CMD [ "python", "./server.py" ]