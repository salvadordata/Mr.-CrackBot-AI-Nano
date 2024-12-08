# Use a stable NVIDIA Jetson base image from JetPack 5.1
FROM nvcr.io/nvidia/l4t-base:r35.1.0

# Set environment variables to avoid interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update system and install required dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install Python dependencies if a requirements.txt file exists
RUN pip3 install --no-cache-dir -r requirements.txt || echo "No requirements.txt found"

# Specify the default command to run the application
CMD ["python3", "main.py"]
