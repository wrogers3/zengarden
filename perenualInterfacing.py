from api_secrets import PERENUAL_API
import requests

# several URLS

def getPlantDetails(ID):
    url = f"https://perenual.com/api/species/details/[{ID}]?key={PERENUAL_API}"
    payload = {}
    headers = {}

    response = requests.request("", url, headers=headers, data=payload)

    print(response.text)


getPlantDetails(1)