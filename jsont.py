import json
import urllib.request, urllib.parse, urllib.error

counts = []

while True:
    url = input('Enter - ')
    data = urllib.request.urlopen(url).read()

    info = json.loads(data)
    print(info)
    comments = info['comments']

    for comment in comments:
        counts.append(comment['count'])

    print('Count:', len(comments))
    print('Sum:', sum(counts))
    break
