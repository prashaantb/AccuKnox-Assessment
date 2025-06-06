import psutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="system_health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Thresholds
CPU_THRESHOLD = 80  # in percent
MEMORY_THRESHOLD = 80  # in percent
DISK_THRESHOLD = 90  # in percent
PROCESS_THRESHOLD = 300  # max number of processes

def check_cpu():
    cpu = psutil.cpu_percent(interval=1)
    if cpu > CPU_THRESHOLD:
        message = f"High CPU usage detected: {cpu}%"
        alert(message)
    return cpu

def check_memory():
    memory = psutil.virtual_memory()
    mem_percent = memory.percent
    if mem_percent > MEMORY_THRESHOLD:
        message = f"High Memory usage detected: {mem_percent}%"
        alert(message)
    return mem_percent

def check_disk():
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    if disk_percent > DISK_THRESHOLD:
        message = f"Low Disk space: {100 - disk_percent}% free"
        alert(message)
    return disk_percent

def check_processes():
    num_processes = len(psutil.pids())
    if num_processes > PROCESS_THRESHOLD:
        message = f"Too many running processes: {num_processes}"
        alert(message)
    return num_processes

def alert(message):
    print("ALERT:", message)
    logging.warning(message)

def log_status(cpu, memory, disk, processes):
    status = (
        f"CPU: {cpu}% | "
        f"Memory: {memory}% | "
        f"Disk: {disk}% | "
        f"Processes: {processes}"
    )
    print(status)
    logging.info(status)

if __name__ == "__main__":
    cpu = check_cpu()
    memory = check_memory()
    disk = check_disk()
    processes = check_processes()
    log_status(cpu, memory, disk, processes)
