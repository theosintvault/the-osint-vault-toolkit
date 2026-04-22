import requests
from bs4 import BeautifulSoup

def search_query(query):
    url = "https://html.duckduckgo.com/html/"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    data = {
        "q": query
    }

    results = []

    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        for a in soup.select(".result__a")[:5]:
            title = a.get_text()
            link = a.get("href")
            results.append({
                "title": title,
                "link": link
            })

    except:
        return {"error": "search failed"}

    return results
