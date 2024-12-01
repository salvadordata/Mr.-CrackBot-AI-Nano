import os
import psutil
import shutil
import subprocess
import platform

# Resource Management
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage(path="/"):
    disk = psutil.disk_usage(path)
    return disk.percent

# GPU Management
def is_gpu_available():
    return shutil.which("nvidia-smi") is not None

def get_gpu_usage():
    try:
        result = subprocess.check_output(["nvidia-smi", "--query-gpu=memory.used,memory.total,utilization.gpu", "--format=csv,noheader,nounits"])
        used_memory, total_memory, utilization = result.decode().strip().split(", ")
        return {
            "used_memory": int(used_memory),
            "total_memory": int(total_memory),
            "utilization": int(utilization)
        }
    except Exception as e:
        print(f"[!] Failed to retrieve GPU usage: {e}")
        return None

# System Capability Checks
def check_minimum_requirements():
    requirements = {
        "cpu": 2.0,
        "memory": 4 * 1024 ** 3,
        "disk": 10 * 1024 ** 3
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
            "disk_total": disk_total
        }
    }

# System Commands
def run_command(command):
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return result.decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(f"[!] Command failed: {e.output.decode('utf-8')}")
        return None

# Performance Optimizations
def set_high_priority():
    try:
        p = psutil.Process(os.getpid())
        p.nice(psutil.HIGH_PRIORITY_CLASS)
        print("[*] Process priority set to high.")
    except Exception as e:
        print(f"[!] Failed to set high priority: {e}")

# System Information
def get_system_info():
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.architecture()[0],
        "cpu": platform.processor(),
        "cores": psutil.cpu_count(logical=True),
        "memory": psutil.virtual_memory().total // (1024 ** 3)
    }
