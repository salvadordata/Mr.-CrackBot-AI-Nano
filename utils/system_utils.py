import os
import platform
import shutil
import subprocess

import psutil


# Resource Management
def get_cpu_usage():
    """
    Get the current CPU usage as a percentage.
    :return: CPU usage percentage.
    """
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    """
    Get the current memory usage as a percentage.
    :return: Memory usage percentage.
    """
    memory = psutil.virtual_memory()
    return memory.percent


def get_disk_usage(path="/"):
    """
    Get the disk usage for the specified path.
    :param path: Path to check disk usage (default: "/").
    :return: Disk usage percentage.
    """
    disk = psutil.disk_usage(path)
    return disk.percent


# GPU Management
def is_gpu_available():
    """
    Check if a GPU is available on the system.
    :return: True if GPU is available, False otherwise.
    """
    return shutil.which("nvidia-smi") is not None


def get_gpu_usage():
    """
    Get the current GPU usage statistics.
    :return: Dictionary with used memory, total memory, and utilization percentage, or None on failure.
    """
    try:
        result = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=memory.used,memory.total,utilization.gpu", "--format=csv,noheader,nounits"]
        )
        used_memory, total_memory, utilization = result.decode().strip().split(", ")
        return {
            "used_memory": int(used_memory),
            "total_memory": int(total_memory),
            "utilization": int(utilization),
        }
    except subprocess.CalledProcessError as e:
        print(f"[!] Failed to retrieve GPU usage: {e}")
        return None


# System Capability Checks
def check_minimum_requirements():
    """
    Check if the system meets minimum hardware requirements.
    :return: Dictionary indicating if requirements are met and details of the system.
    """
    requirements = {
        "cpu": 2.0,  # Minimum CPU speed in GHz
        "memory": 4 * 1024 ** 3,  # Minimum memory in bytes
        "disk": 10 * 1024 ** 3,  # Minimum disk space in bytes
    }

    cpu_speed = psutil.cpu_freq().current / 1000
    memory_total = psutil.virtual_memory().total
    disk_total = psutil.disk_usage("/").total

    return {
        "cpu_ok": cpu_speed >= requirements["cpu"],
        "memory_ok": memory_total >= requirements["memory"],
        "disk_ok": disk_total >= requirements["disk"],
        "details": {
            "cpu_speed": cpu_speed,
            "memory_total": memory_total,
            "disk_total": disk_total,
        },
    }


# System Commands
def run_command(command):
    """
    Run a system command and capture the output.
    :param command: Command to execute as a list of strings.
    :return: Command output as a string, or None on failure.
    """
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return result.decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(f"[!] Command failed: {e.output.decode('utf-8')}")
        return None


# Performance Optimizations
def set_high_priority():
    """
    Set the current process to high priority.
    :return: None
    """
    try:
        p = psutil.Process(os.getpid())
        p.nice(psutil.HIGH_PRIORITY_CLASS)
        print("[*] Process priority set to high.")
    except psutil.AccessDenied as e:
        print(f"[!] Failed to set high priority: {e}")


# System Information
def get_system_info():
    """
    Get detailed information about the system.
    :return: Dictionary with system information.
    """
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.architecture()[0],
        "cpu": platform.processor(),
        "cores": psutil.cpu_count(logical=True),
        "memory": psutil.virtual_memory().total // (1024 ** 3),
    }
