from functions.ping_host import ping_host
from functions.mac_address import get_mac_address
from functions.get_vendor import get_vendor_from_mac
from functions.scan_ports import scan_ports
from functions.get_os import get_os
from functions.network_speed import measure_network_speed
from functions.resolve_domain import resolve_domain
from functions.check_security import check_security_threat
import logging
import pyttsx3
# Initialize text-to-speech engine
engine = pyttsx3.init()


def scan_network(ip, tree, progress, results):
    if ping_host(ip):
        mac_address = get_mac_address(ip)
        vendor = get_vendor_from_mac(mac_address)
        open_ports = scan_ports(ip)
        os = get_os(ip)
        speed = measure_network_speed()
        domain = resolve_domain(ip)
        security_status = check_security_threat(ip)

        result_data = {
            "IP": ip,
            "MAC": mac_address,
            "Vendor": vendor,
            "Open Ports": open_ports,
            "OS": os,
            "Speed": speed,
            "Domain": domain,
            "Security Status": security_status,
        }
        results.append(result_data)

        tree.insert('', 'end', values=(
            ip, mac_address, vendor, ', '.join(map(str, open_ports)),
            os, speed, domain, security_status
        ))
    else:
        tree.insert('', 'end', values=(ip, "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"))
    progress.stop()
    engine.say("Scan complete.")
    engine.runAndWait()
