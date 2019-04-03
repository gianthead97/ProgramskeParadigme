import requests

url = 'https://quotes.rest/god'

response = requests.get(url)

if  response.ok:
    json = response.json()
    print(json)
else:
    print("Neuspesno dohvatanje citata")