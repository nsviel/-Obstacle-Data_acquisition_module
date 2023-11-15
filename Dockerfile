FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive
ENV TZ Europe/Paris

# Install dependancy packages
RUN apt update \
    && apt install -y \
    python3 python3-pip python3-pcapy python3-scapy libiperf0 iputils-ping \
    && pip3 install scapy requests pandas psutil iperf3 \
    && rm -rf /var/lib/apt/lists/*

# Program parameters
COPY . /app/pywardium
VOLUME /app/data
WORKDIR /app/pywardium

# Open port
# HTTP server
EXPOSE 314
# iperf3
EXPOSE 6970

# Final command
CMD [ "python3", "main.py"]
