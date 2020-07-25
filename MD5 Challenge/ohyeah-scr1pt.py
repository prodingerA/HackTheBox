import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://docker.hackthebox.eu:31846/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

print(soup)
