import socket

def scan_ports(ip):
    open_ports = []
    for port in range(80, 85):  # Limiting the port range for easier debugging
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports
