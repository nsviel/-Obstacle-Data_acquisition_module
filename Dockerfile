FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV TZ Europe/Paris

# Install dependancy packages
RUN mkdir app \
    && apt-get update \
    && apt-get install -y sudo python-is-python3 python3-pip python3-pcapy python3-scapy \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install scapy

# Program parameters
COPY . /app
WORKDIR /app

# Open port
EXPOSE 2370

# Final command
CMD [ "python", "main.py"]



