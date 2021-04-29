import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE+"/video/123")

#response = requests.get(BASE+"/video/123")

print(response.json())