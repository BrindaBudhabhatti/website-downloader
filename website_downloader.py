import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import os

url = input('Enter Website URL to Download: ')

# Send a get request
try:
    r = requests.get(url)
except:
    print(f'Cannot send GET Requests to the {url}')


soup = BeautifulSoup(r.content, "html.parser")

# Get list of links
links = []
for i in soup.find_all("a", href=True):
    link = urljoin(url, i['href'])
    # Check if links are not repeated
    if (link not in links):
        links.append(link)

print("links found: ")
print(links)

# Download Pages

# Make Directory to save the project
dir_name = f"Downloaded {urlparse(url).netloc}"
if not (os.path.isdir(dir_name)):
    os.mkdir(dir_name)

temp=1
for link in links:
    r = requests.get(link)

    if r.status_code != 200:
        print(f"Error sending GET Request to the {link}")
        break

    with open(f'{dir_name}/{temp}.html', "wb") as f:
        f.write(r.content)
        print(f'{link} successfully downloaded!')
        temp+=1


print('Website Downloaded!')