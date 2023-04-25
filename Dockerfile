# Base image to be used
FROM python:3.8-slim-buster

# Install the required dependencies
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    && rm -rf /var/lib/apt/lists/*

# Copy the scripts and run it
COPY install_docker_bench.sh /
RUN /bin/bash /install_docker_bench.py / 

COPY install_clair.sh /
RUN /bin/bash /install_clair.py / 

COPY install_trivy.sh /
RUN /bin/bash /install_trivy.py / 

# Copy the Python script 
COPY SRTsploit.py /

# Run the Python script to generate the combined results
CMD ["python", "SRTsploit.py"]
