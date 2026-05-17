import re
import requests
from bs4 import BeautifulSoup

def scrape_all_emails(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Regex for email extraction
        emails = set(re.findall(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
            soup.get_text()
        ))

        return emails

    except Exception as e:
        print("Error:", e)
        return set()


if __name__ == "__main__":
    website_url = input("Enter website URL: ")
    emails = scrape_all_emails(website_url)

    if emails:
        print("\nEmails found:")
        for email in emails:
            print(email)
        print(f"\nTotal emails found: {len(emails)}")
    else:
        print("No emails found.")
