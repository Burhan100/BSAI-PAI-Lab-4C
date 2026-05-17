import re
import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_all_emails(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    emails = set(re.findall(
        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        soup.get_text()
    ))

    return list(emails)


if __name__ == "__main__":
    url = "https://example.com"
    emails = scrape_all_emails(url)

    if emails:
        df = pd.DataFrame(emails, columns=["Email"])
        df.to_excel("scraped_emails.xlsx", index=False)
        print(f"{len(emails)} emails saved to scraped_emails.xlsx")
    else:
        print("No emails found")
