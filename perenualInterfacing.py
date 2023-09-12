from api_secrets import PERENUAL_API
import requests

# several URLS

import requests

url = f"https://perenual.com/api/species-list?key={PERENUAL_API}"

payload = {}
headers = {}

response = requests.request("", url, headers=headers, data=payload)

print(response.text)