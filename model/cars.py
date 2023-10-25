import requests

url = "https://cars-by-api-ninjas.p.rapidapi.com/v1/cars"

modelInput = str(input("What is your car model: "))
querystring = {"model": modelInput}

headers = {
	"X-RapidAPI-Key": "a8491de794msh6676acc5521c4fcp1c5cf8jsn6d99a8656992",
	"X-RapidAPI-Host": "cars-by-api-ninjas.p.rapidapi.com"
}


def responses():
    response = requests.get(url, headers=headers, params=querystring)
    return response


#import requests

#url = "https://cars-by-api-ninjas.p.rapidapi.com/v1/cars"

#headers = {
#    'X-RapidAPI-Key: a8491de794msh6676acc5521c4fcp1c5cf8jsn6d99a8656992'
#    'X-RapidAPI-Host: cars-by-api-ninjas.p.rapidapi.com'
#} 

#model = 'camry'
#api_url = 'https://api.api-ninjas.com/v1/cars?model={}'.format(model)
#response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
#if response.status_code == requests.codes.ok:
#    print(response.text)
#else:
#    print("Error:", response.status_code, response.text)