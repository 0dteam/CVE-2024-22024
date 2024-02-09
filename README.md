# CVE-2024-22024
Check for CVE-2024-22024 vulnerability in Ivanti Connect Secure

> [!WARNING]
> FOR EDUCATIONAL PURPOSE AND AUTHORIZED TESTING ONLY.

### Parameters
- `-u` or `--target_url`: The target Ivanti Connect Secure (ICS) URL or file with list of URLs.

- `-c` or `--attacker_url`: The attacker URL (generate one using Burp Collaborator, ngrok, or by using a unique URL from [Webhook.site](https://webhook.site))

- `-t` or `--timeout`: Timeout in seconds for the request (default is 3 seconds)


### How to use
Testing a single URL:

`python .\cve_2024_22024.py -u http://vpn.example.com -c http://potatodynamicdns.oastify.com`

Testing list of URLs:

`python .\cve_2024_22024.py -u .\urls_list.txt -c http://potatodynamicdns.oastify.com`

Using a different timeout (5 seconds):

`python .\cve_2024_22024.py -u .\urls_list.txt -c http://potatodynamicdns.oastify.com -t 5`

# Credits
Whoever discovered the vulnerability .. I just read the PoC and automated this.

[0dteam website](https://www.0d.ae)
