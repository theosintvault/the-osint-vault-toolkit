import requests

def check_email_reputation(email):
    url = f"https://emailrep.io/{email}"
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "reputation": data.get("reputation"),
            "suspicious": data.get("suspicious"),
            "references": data.get("references"),
        }
    else:
        return {"error": "lookup failed"}
