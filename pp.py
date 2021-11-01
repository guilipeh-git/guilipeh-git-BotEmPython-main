import requests
from bs4 import BeautifulSoup as bs

url = "http://localhost:5500/html.html"

site = requests.get(url)

pagina = bs(url.text)

print(pagina.find_all('<h1>'))