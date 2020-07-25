import requests
from bs4 import BeautifulSoup
import hashlib
import re

url = 'http://docker.hackthebox.eu:31846/'

r=requests.session()
hesch = r.get(url)
hesch = re.search("<h3 align='center'>+.*?</h3>",hesch.text)
hesch = re.search("'>.*<",hesch[0])
hesch = re.search("[^|'|>|<]...................",hesch[0])
hesch=hashlib.md5(hesch[0].encode('utf-8')).hexdigest()

data={'hash': hesch}
hesch = r.post(url = url, data = data)

print(hesch.text)

