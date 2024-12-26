import requests

KNOWN_VENDORS = {
    "AA:6B:03": "Qualcomm",
    "98:40:BB": "Realtek",
    "44:38:39": "Cumulus Networks",
}

def get_vendor_from_mac(mac):
    mac = mac.upper()
    prefix = mac[:8]

    if prefix in KNOWN_VENDORS:
        return KNOWN_VENDORS[prefix]

    url = f"https://api.macaddress.io/v1?apiKey=at_bn4i0fNL9Zrdb1rZR4lixe1RowXKA&output=json&search=44:38:39:ff:ef:57"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        company_name = data.get("vendorDetails", {}).get("companyName", "Unknown Vendor")
        company_address = data.get("vendorDetails", {}).get("companyAddress", "")
        
        if company_name and company_address:
            return f"{company_name}, {company_address}"
        elif company_name:
            return company_name
        else:
            return "Unknown Vendor"
    except requests.exceptions.RequestException as e:
        print(f"Error during MAC vendor lookup: {e}")
        return "Unknown Vendor"