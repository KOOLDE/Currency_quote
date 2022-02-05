# Import modules 
import json
import requests

# Making a get request
def get_requests(URL: str) -> dict:
    global data_formated

    response = requests.get(URL)
    data = response.json()
    data_formated = json.dumps(data, indent=4)

def money(coin: str) -> dict:
    # :moedas -> USD-BRL,EUR-BRL,BTC-BRL
    # https://economia.awesomeapi.com.br/json/last/:moedas
    get_requests(f"https://economia.awesomeapi.com.br/json/last/{coin}")

money("USD-BRL")
