import requests
from bs4 import BeautifulSoup

url = "https://YOUR_WEBSITE_NAME_HERE"

links = []
website = requests.get(url)
website_text = website.text
soup = BeautifulSoup(website_text)

for link in soup.find_all('a'):
    links.append(link.get('href'))

for link in links:
    print(link)

print(len(links))
