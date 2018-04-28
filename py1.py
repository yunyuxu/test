import requests
url = 'https://github.com'
r = requests.get(url).text
print(r)
