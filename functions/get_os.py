import nmap
import logging
def get_os(ip):
    nm = nmap.PortScanner()
    try:
        nm.scan(ip, arguments="-O")
        if 'osmatch' in nm[ip]:
            os = nm[ip]['osmatch'][0]['name']
            return os
        else:
            return "OS information not available"
    except Exception as e:
        logging.error(f"Error during OS fingerprinting: {e}")
        return "Unknown OS"
