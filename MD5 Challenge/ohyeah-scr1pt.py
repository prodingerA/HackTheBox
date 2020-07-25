import requests
from bs4 import BeautifulSoup
import hashlib
import re


website = requests.get('http://docker.hackthebox.eu:31846/')

cont = BeautifulSoup(website.content, 'html.parser')
hesch = cont.find('h3').text
heschInput = cont.find_all('form')

print(hashlib.md5(hesch.encode('utf-8')).hexdigest())





