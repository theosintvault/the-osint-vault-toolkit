from pivot_engine.api.emailrep import check_email_reputation
from pivot_engine.api.gravatar import check_gravatar
from pivot_engine.api.search import search_query
from pivot_engine.api.username_check import check_username_sites

import requests
from bs4 import BeautifulSoup


# -----------------------------
# SEARCH: BING
# -----------------------------
def bing_search(query):
    url = f"https://www.bing.com/search?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    results = []

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        for item in soup.select("li.b_algo")[:5]:
            a = item.find("a")
            if a:
                results.append({
                    "title": a.get_text(),
                    "link": a.get("href")
                })

    except:
        return []

    return results


# -----------------------------
# CLEAN + FILTER
# -----------------------------
def merge_results(results):
    seen = set()
    clean = []

    for r in results:
        link = r.get("link")
        if not link or link in seen:
            continue

        seen.add(link)
        clean.append(r)

    return clean


def filter_results(results, keywords):
    filtered = []

    for r in results:
        text = (r.get("title", "") + r.get("link", "")).lower()

        if any(k in text for k in keywords):
            filtered.append(r)

    return filtered


# -----------------------------
# TYPE DETECTION
# -----------------------------
def is_email(value):
    return "@" in value and "." in value


def is_phone(value):
    digits = "".join(filter(str.isdigit, value))
    return len(digits) >= 10


# -----------------------------
# NORMALIZATION
# -----------------------------
def normalize_phone(value):
    digits = "".join(filter(str.isdigit, value))

    if len(digits) == 10:
        return "+1" + digits

    if len(digits) > 10:
        return "+" + digits

    return digits


def extract_username(email):
    return email.split("@")[0]


# -----------------------------
# CORE ENGINE
# -----------------------------
def run_pivot(entity):
    target = entity.strip().lower()
    pivots = []

    # =========================
    # EMAIL
    # =========================
    if is_email(target):

        username = extract_username(target)

        rep = check_email_reputation(target)
        grav = check_gravatar(target)
        username_hits = check_username_sites([username])

        raw = []
        raw.extend(search_query(target))
        raw.extend(bing_search(target))
        raw.extend(search_query(username))
        raw.extend(bing_search(username))

        merged = merge_results(raw)

        pivots.append({
            "step": "email reputation",
            "result": rep
        })

        pivots.append({
            "step": "gravatar",
            "result": grav
        })

        pivots.append({
            "step": "username (exact)",
            "result": username_hits
        })

        pivots.append({
            "step": "search",
            "result": merged[:10]
        })

    # =========================
    # PHONE
    # =========================
    elif is_phone(target):

        phone = normalize_phone(target)

        variations = [
            phone,
            phone.replace("+1", ""),
            phone.replace("+", ""),
            f'"{phone}"',
            f'"{phone.replace("+1", "")}"'
        ]

        raw = []

        for v in variations:
            raw.extend(search_query(v))
            raw.extend(bing_search(v))

        merged = merge_results(raw)

        keywords = [
            phone[-10:],
            "contact",
            "phone",
            "call",
            "business",
            "llc"
        ]

        filtered = filter_results(merged, keywords)

        pivots.append({
            "step": "phone intelligence",
            "result": filtered[:10]
        })

    # =========================
    # USERNAME
    # =========================
    else:

        username_hits = check_username_sites([target])

        raw = []
        raw.extend(search_query(target))
        raw.extend(bing_search(target))

        merged = merge_results(raw)

        pivots.append({
            "step": "username",
            "result": username_hits
        })

        pivots.append({
            "step": "search",
            "result": merged[:10]
        })

    return {
        "entity": entity,
        "pivots": pivots
    }
