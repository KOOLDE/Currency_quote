"""
{
    'USDBRL': {
        'code': 'USD', 
        'codein': 'BRL', 
        'name': 'Dólar Americano/Real Brasileiro', 
        'high': '5.3502', 
        'low': '5.2793', 
        'varBid': '0.0445', 
        'pctChange': '0.84', 
        'bid': '5.3279', 
        'ask': '5.3289', 
        'timestamp': '1644010199', 
        'create_date': '2022-02-04 18:29:59'
    }
}
"""

# Import modules 
import json
import requests

# Making a get request
def get_requests(URL: str) -> dict:
    global data
    response = requests.get(URL)
    data = response.json()

def money(coin: str) -> dict:
    # :moedas -> USD-BRL,EUR-BRL,BTC-BRL
    # https://economia.awesomeapi.com.br/json/last/:moedas
    get_requests(f"https://economia.awesomeapi.com.br/json/last/{coin}")

money("USD-BRL")