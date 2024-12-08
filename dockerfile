# Use the latest NVIDIA Jetson base image
FROM nvcr.io/nvidia/l4t-base:latest

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Update system and install required dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install Python dependencies (if any)
RUN pip3 install --no-cache-dir -r requirements.txt

# Specify the default command to run the application
CMD ["python3", "main.py"]