import requests

def jokes():
    url = "https://dad-jokes7.p.rapidapi.com/dad-jokes/random"

    headers = {
        "X-RapidAPI-Key": "Your API KEY here",
        "X-RapidAPI-Host": "dad-jokes7.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    joke = response.json()['joke']
    print(joke) 