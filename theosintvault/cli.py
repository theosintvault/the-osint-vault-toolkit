import argparse
import json
import re
import urllib.parse
from pathlib import Path


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
    """Load JSON platform lists from the data directory."""
    path = DATA_DIR / f"{kind}.json"
    if not path.exists():
        return []
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def classify(entity: str) -> str:
    """Determine what type of entity the user entered."""
    e = entity.strip()
    if EMAIL_RE.match(e):
        return "email"
    if PHONE_RE.match(e):
        return "phone"
    if URL_RE.match(e):
        return "url"
    if USERNAME_RE.match(e):
        return "username"
    return "domain"


# ----------------------------------------
# PIVOT ENGINES
# ----------------------------------------

def pivots_email(entity: str):
    q = urllib.parse.quote_plus(entity)
    local = entity.split("@", 1)[0]

    base = [
        {"label": "HaveIBeenPwned", "category": "breach", "url": f"https://haveibeenpwned.com/account/{q}"},
        {"label": "Gravatar", "category": "avatar", "url": f"https://en.gravatar.com/site/check/{q}"},
        {"label": "Hunter.io", "category": "email-intel", "url": f"https://hunter.io/email-verifier/{q}"},
        {"label": "EmailRep", "category": "reputation", "url": f"https://emailrep.io/{q}"},
        {"label": "Google", "category": "search", "url": f'https://www.google.com/search?q="{q}"'},
        {"label": "DuckDuckGo", "category": "search", "url": f"https://duckduckgo.com/?q={q}"},
        {"label": "Local-part pivot", "category": "username-pivot", "url": f'https://www.google.com/search?q="{local}"'},
    ]

    extra = []
    for p in load_platforms("emails"):
        url = p["url_template"].replace("{q}", q)
        extra.append({"label": p["label"], "category": p["category"], "url": url})

    return base + extra


def pivots_username(entity: str):
    q = urllib.parse.quote_plus(entity)

    base = [
        {"label": "WhatsMyName", "category": "meta-enum", "url": f"https://whatsmyname.app/?q={q}"},
        {"label": "Namechk", "category": "meta-enum", "url": f"https://namechk.com/{q}"},
        {"label": "Google", "category": "search", "url": f'https://www.google.com/search?q="{q}"'},
        {"label": "DuckDuckGo", "category": "search", "url": f"https://duckduckgo.com/?q={q}"},
        {"label": "GitHub Users", "category": "code", "url": f"https://github.com/search?q={q}&type=users"},
        {"label": "Reddit Search", "category": "social", "url": f"https://www.reddit.com/search/?q={q}"},
    ]

    extra = []
    for p in load_platforms("usernames"):
        url = p["url_template"].replace("{q}", q)
        extra.append({"label": p["label"], "category": p["category"], "url": url})

    return base + extra


def pivots_domain(entity: str):
    domain = entity.strip()
    if URL_RE.match(domain):
        domain = re.sub(r"^https?://", "", domain, flags=re.IGNORECASE).split("/", 1)[0]

    d = urllib.parse.quote_plus(domain)

    base = [
        {"label": "crt.sh", "category": "ct-logs", "url": f"https://crt.sh/?q=%25{d}"},
        {"label": "SecurityTrails", "category": "infra", "url": f"https://securitytrails.com/domain/{domain}"},
        {"label": "ViewDNS", "category": "infra", "url": f"https://viewdns.info/dnsrecord/?domain={d}"},
        {"label": "URLScan", "category": "web-scan", "url": f"https://urlscan.io/search/#domain:{d}"},
        {"label": "Shodan", "category": "infra-scan", "url": f"https://www.shodan.io/search?query={d}"},
        {"label": "Censys", "category": "infra-scan", "url": f"https://search.censys.io/search?resource=hosts&q={d}"},
        {"label": "Wayback", "category": "archive", "url": f"https://web.archive.org/web/*/{domain}"},
    ]

    extra = []
    for p in load_platforms("domains"):
        url = (
            p["url_template"]
            .replace("{q}", d)
            .replace("{domain}", domain)
        )
        extra.append({"label": p["label"], "category": p["category"], "url": url})

    return base + extra


def pivots_phone(entity: str):
    digits = re.sub(r"[^\d+]", "", entity)
    q = urllib.parse.quote_plus(digits)

    base = [
        {"label": "SpyDialer", "category": "phone-reverse", "url": "https://www.spydialer.com"},
        {"label": "Truecaller", "category": "phone-reverse", "url": f"https://www.truecaller.com/search/{q}"},
        {"label": "ThisNumber", "category": "phone-reverse", "url": f"https://www.thisnumber.com/phone/{q}/"},
        {"label": "Google", "category": "search", "url": f'https://www.google.com/search?q="{q}"'},
        {"label": "DuckDuckGo", "category": "search", "url": f"https://duckduckgo.com/?q={q}"},
    ]

    extra = []
    for p in load_platforms("phones"):
        url = p["url_template"].replace("{q}", q)
        extra.append({"label": p["label"], "category": p["category"], "url": url})

    return base + extra


# ----------------------------------------
# DOMAIN SCAN ENGINE
# ----------------------------------------

def scan_domain(domain: str):
    d = urllib.parse.quote_plus(domain)

    return {
        "domain": domain,
        "intel": [
            {"label": "crt.sh", "category": "ct-logs", "url": f"https://crt.sh
