# import subprocess
# import re
# import logging
# import os
# def get_mac_address(ip):
#     try:
#         # Ping the device to ensure it's in the ARP cache
#         subprocess.run(['ping', '-c', '1' if os.name != 'nt' else '-n', '1', ip], capture_output=True)
#         # Run arp -a command
#         result = subprocess.run(['arp', '-a', ip], capture_output=True, text=True)
#         if result.returncode == 0:
#             mac_match = re.search(r'([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}', result.stdout)
#             if mac_match:
#                 return mac_match.group(0)
#         return "Unknown MAC"
#     except Exception as e:
#         logging.error(f"Error retrieving MAC address for {ip}: {e}")
#         return "Unknown MAC"

from scapy.all import ARP, Ether, srp
import logging

def get_mac_address(ip):
    try:
        # Create an Ethernet frame with ARP request
        arp_request = ARP(pdst=ip)
        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request

        # Send the packet on the network and capture the response
        answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        # Check if we got a response
        if answered_list:
            return answered_list[0][1].hwsrc  # MAC address is in the hardware source field
        return "Unknown MAC"
    except Exception as e:
        logging.error(f"Error retrieving MAC address for {ip}: {e}")
        return "Unknown MAC"
