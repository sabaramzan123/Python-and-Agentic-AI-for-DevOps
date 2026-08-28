#create a function that can be resued it shows the system info
import psutil

def get_system_details():
    
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        system_info = {
            "cpu": cpu,
            "memory": memory,
            "disk": disk
        }
        return system_info

