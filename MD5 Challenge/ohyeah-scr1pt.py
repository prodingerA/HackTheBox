import requests
from bs4 import BeautifulSoup

website = requests.get('http://docker.hackthebox.eu:31846/')

cont = BeautifulSoup(page.content, 'html.parser')
innerH = soup.find('h3').text

print(innerH)
