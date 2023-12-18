import requests

url = "https://league-of-legends-esports.p.rapidapi.com/statics"

querystring = {"period":"<REQUIRED>"}

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "league-of-legends-esports.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
