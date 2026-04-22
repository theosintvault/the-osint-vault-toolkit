import hashlib
import requests

def check_gravatar(email):
    email_clean = email.strip().lower()
    email_hash = hashlib.md5(email_clean.encode()).hexdigest()

    url = f"https://www.gravatar.com/avatar/{email_hash}?d=404"

    response = requests.get(url)

    if response.status_code == 200:
        return {"gravatar": True}
    else:
        return {"gravatar": False}
