import json
import requests

url = 'http://127.0.0.1:5000/query'
r = requests.post(url,data={'query':input()})
print(r.text)
