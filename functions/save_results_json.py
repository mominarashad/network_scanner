import json
import logging

def save_results_json(results):
    with open('scan_results.json', 'w') as file:
        json.dump(results, file, indent=4)
    logging.info("Scan results saved to JSON.")
