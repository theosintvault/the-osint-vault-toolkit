import time

time.sleep(1)

import requests

def check_email_reputation(email):
    url = f"https://emailrep.io/{email}"

    headers = {
        "User-Agent": "osintvault-cli"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return {
                "reputation": data.get("reputation"),
                "suspicious": data.get("suspicious"),
                "references": data.get("references"),
            }
        else:
            return {
                "error": f"status {response.status_code}"
            }

    except Exception as e:
        return {
            "error": str(e)
        }
