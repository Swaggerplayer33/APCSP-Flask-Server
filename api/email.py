import requests

url = "https://rapidprod-sendgrid-v1.p.rapidapi.com/"

payload = {
	"type": "stats_notification",
	"email_to": "example@test.com",
	"frequency": "daily"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "a8491de794msh6676acc5521c4fcp1c5cf8jsn6d99a8656992",
	"X-RapidAPI-Host": "rapidprod-sendgrid-v1.p.rapidapi.com"
}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())