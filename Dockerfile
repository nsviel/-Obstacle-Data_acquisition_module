FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV TZ Europe/Paris

# Install dependancy packages
RUN mkdir app \
    && apt-get update \
    && apt-get install -y \
    python3 python3-pip python3-pcapy python3-scapy \
    && pip3 install dearpygui scapy requests pandas psutil \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Program parameters
COPY . /app/pywardium
WORKDIR /app/pywardium

# Open port
EXPOSE 314

# Final command
CMD [ "python3", "main.py"]



