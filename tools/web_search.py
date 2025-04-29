import requests
from bs4 import BeautifulSoup

class WebSearchTool:
    def __init__(self):
        self.name = "WebSearchTool"

    def __call__(self, query):
        url = f"https://duckduckgo.com/html/?q={query.replace(' ', '+')}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        results = []

        for result in soup.select('.result__snippet', limit=3):
            text = result.get_text()
            if text:
                results.append(text.strip())

        if not results:
            return "Tidak ada hasil ditemukan."
        return "\n\n".join(results)


# bisa di ganti oleh API resmi