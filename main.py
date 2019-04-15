from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url = 'https://risibank.fr/stickers/hasard'
headers={'User-Agent': 'Mozilla/5.0'}

req = Request(url, headers=headers)
soup = BeautifulSoup(urlopen(req).read(), "html.parser")
link = soup.find("img", class_="img-preview-big")
print(link["src"])
