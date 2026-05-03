[
import argparse
import json
import re
import urllib.parse
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

# ----------------------------------------
# CONSTANTS & REGEX
# ----------------------------------------
DATA_DIR = Path(__file__).resolve().parent / "data"
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
URL_RE = re.compile(r"^https?://", re.IGNORECASE)
USERNAME_RE = re.compile(r"^[A-Za-z0-9_.-]{3,}$")
PHONE_RE = re.compile(r"^\+?[0-9][0-9\s().-]{6,}$")

# ----------------------------------------
# HELPERS
# ----------------------------------------
def load_platforms(kind: str):
    path = DATA_DIR / f"{kind}.json"
    if not path.exists(): return []
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception: return []

def classify(entity: str) -> str:
    e = entity.strip()
    if EMAIL_RE.match(e): return "email"
    if PHONE_RE.match(e): return "phone"
    if URL_RE.match(e): return "url"
    if USERNAME_RE.match(e): return "username"
    return "domain"

# ----------------------------------------
# PIVOT ENGINES
# ----------------------------------------
def pivots_email(entity: str):
    q = urllib.parse.quote_plus(entity)
    base = [{"label": "HaveIBeenPwned", "url": f"https://haveibeenpwned.com/account/{q}"}]
    return base

def pivots_username(entity: str):
    q = urllib.parse.quote_plus(entity)
    base = [{"label": "GitHub", "url": f"https://github.com/{q}"}]
    return base

# ----------------------------------------
# EXECUTION ENGINE (The Missing Piece)
# ----------------------------------------
def main():
    parser = argparse.ArgumentParser(description='VaultX: Elite OSINT Engine')
    parser.add_argument('target', help='Target to trace')
    args = parser.parse_args()

    target = args.target
    kind = classify(target)
    print(f"{Fore.CYAN}[*] Target Classified as: {kind.upper()}")

    results = []
    if kind == "email": results = pivots_email(target)
    elif kind == "username": results = pivots_username(target)
    
    for res in results:
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] {res['label']}: {res['url']}")

if __name__ == "__main__":
    main()
    ]
