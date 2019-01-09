import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter - ')
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)

sum = 0
for count in tree.findall('./comments/comment'):
    n = count.find('count').text
    sum = sum + int(n)

print(sum)
