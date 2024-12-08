# Use a stable CUDA base image
FROM nvcr.io/nvidia/cuda:11.4.2-base-ubuntu20.04

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Update system and install required dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install Python dependencies if they exist
RUN pip3 install --no-cache-dir -r requirements.txt || echo "No requirements.txt found"

# Specify the default command
CMD ["python3", "main.py"]
