import requests

url = "https://cars-by-api-ninjas.p.rapidapi.com/v1/cars"

modelInput = str(input("What is your car model: "))
querystring = {"model": modelInput}

headers = {
    "X-RapidAPI-Key": "a8491de794msh6676acc5521c4fcp1c5cf8jsn6d99a8656992",
    "X-RapidAPI-Host": "cars-by-api-ninjas.p.rapidapi.com"
}

def get_car_info():
    response = requests.get(url, headers=headers, params=querystring)
    return response

response = get_car_info()

if response.status_code == 200:
    car_data = response.json()
    print("Car Information:")
    print(car_data)
else:
    print("Error:", response.status_code, response.text)

