import requests

url_rankings = "https://www.ufc.com.br/rankings"

response = requests.get(url_rankings)

print(response)