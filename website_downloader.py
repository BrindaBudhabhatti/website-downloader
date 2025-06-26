import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import os

url = "https://cyber-wise-pi.vercel.app/"


# Send a get request
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

# Get list of links
links = []
for i in soup.find_all("a", href=True):
    # Check if links are not repeated
    if (i['href'] not in links):
        links.append(i['href'])

print("links found: ")
print(links)

# # Download Pages

# # Make Dir
# os.mkdir(f'Downloade_{url}_by_b')

# for i in links: 

#     # with open(f"Downloade_{url}_by_b/")

# ------------------------------------------------------- 

# Download Pages

# Make Directory to save the project
dir_name = f"Downloaded {urlparse("https://cyber-wise-pi.vercel.app/").netloc}"
if not (os.path.isdir(dir_name)):
    os.mkdir(dir_name)

temp=1
for i in links:
    link = f"{url[:-1]}{i}"

    r = requests.get(link)

    if r.status_code != 200:
        print("Error sending GET Request to the {link}")
        break

    with open(f'{dir_name}/{temp}.html', "wb") as f:
        f.write(r.content)
        print('{link} successfully downloaded!')
        temp+=1


print('Website Downloaded!')