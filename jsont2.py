import json
import urllib.request, urllib.parse, urllib.error

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    parms = dict()
    parms['address'] = address
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')


    js = json.loads(data)

    print('Place ID ', js["results"][0]["place_id"])
