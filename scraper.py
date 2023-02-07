import requests
from bs4 import BeautifulSoup

URL = "https://www.vstart.dev/plays"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
plays = soup.find(id="playCards")

print(plays.prettify())