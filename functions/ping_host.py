import subprocess
import logging
def ping_host(ip):
    try:
        response = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)
        return response.returncode == 0
    except Exception as e:
        logging.error(f"Error pinging IP {ip}: {e}")
        return False
