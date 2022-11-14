FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive
ENV TZ Europe/Paris

# Install dependancy packages
RUN apt update \
    && apt install -y \
    python3 python3-pip python3-pcapy python3-scapy libiperf0 \
    && pip3 install scapy requests pandas psutil iperf3 \
    && apt clean \
    && rm -rf /var/lib/apt/lists/* \
    && apt autoremove -y

# Program parameters
COPY . /app/pywardium
VOLUME /app/hubium/data
WORKDIR /app/pywardium

# Open port
EXPOSE 314  # HTTP server
EXPOSE 6970 # iperf3

# Final command
CMD [ "python3", "main.py"]
