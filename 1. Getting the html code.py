import requests
from bs4 import BeautifulSoup
import html5lib
import lxml

website ="https://subslikescript.com/movie/Blind_Detective-2332707"
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'html5lib')
print(soup.prettify())




