import psutil
import logging
import time

#logging
logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

#Thresholds
CPU_THRESHOLD = 80.0  #percentage
MEMORY_THRESHOLD = 80.0  #percentage
DISK_THRESHOLD = 80.0  #percentage

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
    return cpu_usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High memory usage detected: {memory_usage}%')
    return memory_usage

def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'High disk usage detected: {disk_usage}%')
    return disk_usage

def check_running_processes():
    processes = [proc.info for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent'])]
    logging.info(f'Running processes: {processes}')
    return processes

def monitor_system_health():
    while True:
        cpu_usage = check_cpu_usage()
        memory_usage = check_memory_usage()
        disk_usage = check_disk_usage()
        processes = check_running_processes()
        
        logging.info(f'System Health - CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%')
        
        time.sleep(60)  #sleep 60 s before next check

if __name__ == "__main__":
    monitor_system_health()