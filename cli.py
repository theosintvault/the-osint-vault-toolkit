import argparse
import json
import re
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

init(autoreset=True)

# Advanced Regex for instant classification
EMAIL_RE = re.compile(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$', re.I)
PHONE_RE = re.compile(r'^\+?1?\d{9,15}$')
USERNAME_RE = re.compile(r'^[a-zA-Z0-9._-]{3,25}$')

DATA_DIR = Path('data')

def load_data(kind):
    path = DATA_DIR / f"{kind}.json"
    return json.load(open(path, 'r')) if path.exists() else []

def verify_site(label, url_template, query):
    target_url = url_template.replace("{q}", query)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0.0.0"}
    try:
        # allow_redirects=False prevents false positives from login redirects
        r = requests.get(target_url, headers=headers, timeout=5, allow_redirects=False)
        if r.status_code == 200:
            print(f"[{Fore.GREEN}FOUND{Style.RESET_ALL}] {label}: {target_url}")
            return target_url
    except:
        pass
    return None

def main():
    parser = argparse.ArgumentParser(description='VaultTracer: High-Fidelity OSINT')
    parser.add_argument('target', help='Username, Email, or Phone Number')
    args = parser.parse_args()

    target = args.target
    data_type = 'usernames' # Default

    if EMAIL_RE.match(target):
        print(f"{Fore.CYAN}Target Type: EMAIL")
        data_type = 'email'
    elif PHONE_RE.match(target):
        print(f"{Fore.CYAN}Target Type: PHONE")
        data_type = 'phone'
    else:
        print(f"{Fore.CYAN}Target Type: USERNAME")

    platforms = load_data(data_type)
    
    print(f"[*] Scanning {len(platforms)} vectors...\n")
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(lambda p: verify_site(p['label'], p['url_template'], target), platforms)

if __name__ == '__main__':
    main()
