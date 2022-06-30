FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV TZ Europe/Paris

# Install dependancy packages
RUN mkdir app \
    && apt-get update \
    && apt-get install -y \
    python3 python3-pip python3-pcapy python3-scapy \
    libx11-6 libgl1-mesa-glx libgl1-mesa-dri \
    && pip3 install dearpygui scapy requests pandas \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Program parameters
COPY . /app
WORKDIR /app

# Open port
EXPOSE 2369
EXPOSE 2370 

# Final command
CMD [ "python3", "main.py"]



