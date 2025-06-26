import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os

url = "https://cyber-wise-pi.vercel.app/"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

# Get list of links
links = []
for i in soup.find_all("a", href=True):
    # Check if Links are not repeated
    if i['href'] not in links:
        links.append(i['href'])

print("Links found: ")
print(links)

# Download Pages

# Make Dir
os.mkdir(f'Downloade_{url}_by_b')
