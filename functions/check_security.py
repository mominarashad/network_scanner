import requests
import logging
def check_security_threat(ip):
    try:
        url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
        headers = {'x-apikey': '2487cc2f854cfab085206bb69ff362d43b46bf80adf9e77e537fcefbacd2bdd8'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            threat_status = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
            if threat_status:
                return f"Malicious activity found: {threat_status.get('malicious', 0)} threats"
            else:
                return "No malicious activity detected"
        else:
            return "Unable to check security status"
    except requests.exceptions.RequestException as e:
        logging.error(f"Error checking security threat for {ip}: {e}")
        return "Error fetching security data"
