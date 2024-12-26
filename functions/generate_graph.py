import matplotlib.pyplot as plt
import logging
def generate_graph(results):
    ip_addresses = [res['IP'] for res in results]
    open_ports = [len(res['Open Ports']) for res in results]
    plt.bar(ip_addresses, open_ports, color='blue')
    plt.xlabel('IP Addresses')
    plt.ylabel('Number of Open Ports')
    plt.title('Open Ports by IP Address')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('report.png')
    plt.show()
    logging.info("Graphical report generated.")
