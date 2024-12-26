import ipaddress
from functions.scan_network import scan_network

def scan_range(ip_range, tree, progress, results):
    network = ipaddress.IPv4Network(ip_range, strict=False)
    for ip in network.hosts():
        scan_network(str(ip), tree, progress, results)
