import requests
url = "http://icanhazdadjoke.com"

response = requests.get(url, headers={"Accept": "application/json"})

data = response.json()

print(data["joke"])