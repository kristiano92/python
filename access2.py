import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1

tags = soup('a')
n = 0
for tag in tags:
    if n <= count:
        n = n + 1
        print ('Retrieving:', url)
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        url = tags[position].get('href', None)
