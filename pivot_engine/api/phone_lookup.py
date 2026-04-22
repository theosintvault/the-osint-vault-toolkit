import requests

def phone_lookup(phone):
    try:
        url = f"http://apilayer.net/api/validate?access_key=YOUR_KEY&number={phone}"
        r = requests.get(url, timeout=10)
        data = r.json()

        return {
            "valid": data.get("valid"),
            "country": data.get("country_name"),
            "location": data.get("location"),
            "carrier": data.get("carrier"),
            "line_type": data.get("line_type"),
        }

    except:
        return {"error": "lookup failed"}
