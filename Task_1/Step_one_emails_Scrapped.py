import re
import requests
from bs4 import BeautifulSoup

def scrape_one_email(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    emails = set(re.findall(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        soup.get_text()
    ))

    if emails:
        return list(emails)
    return None


if __name__ == "__main__":
    url = "https://example.com"
    email = scrape_one_email(url)

    if email:
        print("Email found:", email)
    else:
        print("No email found")
