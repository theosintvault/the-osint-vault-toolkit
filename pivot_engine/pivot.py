import requests
from bs4 import BeautifulSoup
import re


# =========================
# SEARCH ENGINE
# =========================
def search_engine(query):
    results = []
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        r = requests.post(
            "https://html.duckduckgo.com/html/",
            data={"q": query},
            headers=headers,
            timeout=10
        )
        soup = BeautifulSoup(r.text, "html.parser")

        for a in soup.select("a.result__a")[:5]:
            results.append({
                "title": a.get_text(),
                "link": a.get("href")
            })
    except:
        pass

    try:
        r = requests.get(
            f"https://www.bing.com/search?q={query}",
            headers=headers,
            timeout=10
        )
        soup = BeautifulSoup(r.text, "html.parser")

        for item in soup.select("li.b_algo")[:5]:
            a = item.find("a")
            if a:
                results.append({
                    "title": a.get_text(),
                    "link": a.get("href")
                })
    except:
        pass

    return results


# =========================
# SPYDIALER LOOKUP
# =========================
def spydialer_lookup(phone):
    url = f"https://www.spydialer.com/{phone}"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        r = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        text = soup.get_text().lower()

        result = {}

        if "name:" in text:
            result["possible_name"] = True

        if "wireless" in text:
            result["line_type"] = "wireless"

        if "landline" in text:
            result["line_type"] = "landline"

        if "voip" in text:
            result["line_type"] = "voip"

        return result if result else {"result": "no data found"}

    except:
        return {"error": "spydialer failed"}


# =========================
# CLEAN RESULTS
# =========================
def clean_results(results):
    seen = set()
    clean = []

    for r in results:
        link = r.get("link")

        if not link or link in seen:
            continue

        if any(x in link.lower() for x in ["login", "signup", "google.com"]):
            continue

        seen.add(link)
        clean.append(r)

    return clean


# =========================
# DOMAIN EXTRACTION
# =========================
def extract_domains(results):
    domains = set()

    for r in results:
        link = r.get("link", "")
        match = re.findall(r"https?://([^/]+)/?", link)

        if match:
            domains.add(match[0])

    return list(domains)


# =========================
# TYPE DETECTION
# =========================
def is_email(v):
    return "@" in v and "." in v


def is_phone(v):
    digits = "".join(filter(str.isdigit, v))
    return len(digits) >= 10


# =========================
# NORMALIZE PHONE
# =========================
def normalize_phone(v):
    digits = "".join(filter(str.isdigit, v))

    if len(digits) == 10:
        return "+1" + digits

    if len(digits) > 10:
        return "+" + digits

    return digits


# =========================
# CORE ENGINE
# =========================
def run_pivot(entity):
    target = entity.strip().lower()
    raw = []
    pivots = []

    # EMAIL
    if is_email(target):
        username = target.split("@")[0]

        raw.extend(search_engine(target))
        raw.extend(search_engine(username))

    # PHONE
    elif is_phone(target):
        phone = normalize_phone(target)

        spy = spydialer_lookup(phone)

        pivots.append({
            "step": "spydialer",
            "result": spy
        })

        variations = [
            phone,
            phone.replace("+1", ""),
            f'"{phone}"',
            f'"{phone.replace("+1", "")}"'
        ]

        for v in variations:
            raw.extend(search_engine(v))

    # USERNAME
    else:
        raw.extend(search_engine(target))

    cleaned = clean_results(raw)
    domains = extract_domains(cleaned)

    pivots.append({"step": "results", "result": cleaned[:10]})
    pivots.append({"step": "domains", "result": domains})

    return {
        "entity": entity,
        "pivots": pivots
    }
