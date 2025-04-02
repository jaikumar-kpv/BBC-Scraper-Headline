import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("h2")  # Update class if needed

print("Latest BBC News Headlines with Links:")
for i, headline in enumerate(headlines, 1):
    headline_text = headline.get_text(strip=True)
    link = headline.find_parent("a")["href"] if headline.find_parent("a") else "No link found"
    full_link = f"https://www.bbc.com{link}" if link.startswith("/") else link
    
    print(f"{i}. {headline_text}")
    print(f"   Link: {full_link}\n")  # Emoji replaced with "Link:"