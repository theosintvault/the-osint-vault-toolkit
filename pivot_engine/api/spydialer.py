import requests
from bs4 import BeautifulSoup

def spydialer_lookup(phone):
    url = f"https://www.spydialer.com/{phone}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

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
