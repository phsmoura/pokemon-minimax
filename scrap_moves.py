import requests
from bs4 import BeautifulSoup

session = requests.session()
url = 'https://pokemondb.net/move/all'

response = session.get(url)
# print(response)

content = response.text
# print(content)

soup = BeautifulSoup(content,features="html.parser")
header = soup.find_all("table")[0]

print(header)