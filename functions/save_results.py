import pandas as pd
import logging

def save_results_csv(results):
    df = pd.DataFrame(results)
    df.to_csv('scan_results.csv', index=False)
    logging.info("Scan results saved to CSV.")
