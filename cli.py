import argparse
import json
import re
import requests
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

init(autoreset=True)

EMAIL_RE = re.compile(r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$', re.I)
PHONE_RE = re.compile(r'^\+?1?\d{9,15}$')
USERNAME_RE = re.compile(r'^[a-zA-Z0-9._-]{3,25}$')

# Ensures it finds the data folder in the root
DATA_DIR = Path(__file__).resolve().parent / "data"

def load_data(kind):
    path = DATA_DIR / f"{kind}.json"
    if not path.exists():
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def verify_site(label, url_template, query):
    target_url = url_template.replace("{q}", query)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/119.0.0.0"}
    try:
        r = requests.get(target_url, headers=headers, timeout=5, allow_redirects=False)
        if r.status_code == 200:
            print(f"[{Fore.GREEN}FOUND{Style.RESET_ALL}] {label}: {target_url}")
            return target_url
    except:
        pass
    return None

def main():
    parser = argparse.ArgumentParser(description='VaultX: Elite OSINT Engine')
    parser.add_argument('target', help='Target to trace')
    args = parser.parse_args()

    target = args.target
    data_type = 'usernames'

    if EMAIL_RE.match(target):
        print(f"{Fore.CYAN}[*] Target Type: EMAIL")
        data_type = 'email'
    elif PHONE_RE.match(target):
        print(f"{Fore.CYAN}[*] Target Type: PHONE")
        data_type = 'phone'
    else:
        print(f"{Fore.CYAN}[*] Target Type: USERNAME")

    platforms = load_data(data_type)
    print(f"[*] Scanning {len(platforms)} vectors from {DATA_DIR}...\n")
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(lambda p: verify_site(p['label'], p['url_template'], target), platforms)

if __name__ == '__main__':
    main()
