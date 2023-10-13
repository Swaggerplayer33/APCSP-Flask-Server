import requests

url = "rapidapi.com"

headers = {
    'X-RapidAPI-Key: a8491de794msh6676acc5521c4fcp1c5cf8jsn6d99a8656992'
    'X-RapidAPI-Host: cars-by-api-ninjas.p.rapidapi.com'
} 

import requests

model = 'camry'
api_url = 'https://api.api-ninjas.com/v1/cars?model={}'.format(model)
response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)