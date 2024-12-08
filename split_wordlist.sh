#!/bin/bash

# Paths
rockyou_path="data/rockyou2024.txt"
split_output_dir="data/split_rockyou"

# Create output directory if it doesn't exist
mkdir -p $split_output_dir

# Split the file into chunks
if [ -f "$rockyou_path" ]; then
    echo "Splitting rockyou2024.txt..."
    split -l 100000 $rockyou_path $split_output_dir/rockyou_part_
    echo "File split into parts in $split_output_dir"
else
    echo "File $rockyou_path does not exist. Please download it first."
fi