import requests
from bs4 import BeautifulSoup

URL = "https://www.geeksforgeeks.org/data-structures/"
req = requests.get(URL)

soup = BeautifulSoup(req.content, 'html5lib')

res = soup.title

print(soup.get_text())