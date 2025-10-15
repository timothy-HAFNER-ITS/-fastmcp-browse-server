import requests
from bs4 import BeautifulSoup

def browse_url(url: str, keyword: str = None):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(separator=' ', strip=True)
        result = {"html": html}
        if keyword:
            count = text.lower().count(keyword.lower())
            result["keyword"] = keyword
            result["count"] = count
            result["found"] = count > 0
            result["matches"] = []
            if count > 0:
                # Find all matching sentences (simple approach)
                sentences = [s.strip() for s in text.split('.') if keyword.lower() in s.lower()]
                result["matches"] = sentences
        return result
    except Exception as e:
        return {"error": str(e)}