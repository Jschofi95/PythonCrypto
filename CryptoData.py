from requests import Session
import json

# This is a test
# This is another test line

quotes_latest_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest' # The URL to the Coin Market Cap latest quotes database

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "099b0231-cdb1-482b-8921-4b95af9590fa"
}

session = Session()
session.headers.update(headers)

cryptoID = {'btc': '1', 'eth': '1027', 'ada': '2010', 'xrp': '52', 'ltc': '2', 'xlm': '512', 'bnb': '1839', 'doge': '74', 'usdt': '825'} # Contains each crypto name ID paired with their id within the API
dataNames = ["last_updated", "market_cap", "percent_change_1h", "percent_change_24h", "percent_change_7d", "percent_change_30d", "percent_change_60d", "percent_change_90d", "volume_24h", "price"] # List of all the supported types of data that the user can access about a particular crypto

# General Description
#   Gets the price data of crypto currencies supported by the "Coin Market Cap API"
#
# Parameters
#   (type) crypto type such as "btc", "eth", "ada", etc
#   (data_name) the data in which the user wants, such as "price", "last_updated", "percent_change_1h", etc
#
def getLatestData(type, data_name):
    data_name = data_name.lower()
    type = type.lower()
    crypto_param = get_param(type) # Assigns a dictionary of the corresponding crypto and currency type4

    response = session.get(quotes_latest_url, params=crypto_param)

    # Checks if the data_name variable is a correct type of data supported by the API
    if data_name not in dataNames:
        print("Incorrect data type \"{}\". \nUsage: ".format(data_name), end=" ")
        for name in dataNames:
            print("\"{}\"".format(name), end=" ")
        return -1

    for name in dataNames:
        if data_name == name:
            return json.loads(response.text)['data'][cryptoID[type]]['quote']['USD'][name] # Pulls the desired information from the json data supplied by the API


def listSupportedCryptoCurrencies():
    myList = []
    for id in cryptoID:
        myList.append(id)
    return myList


# General Description
#   Returns the correct dictionary corresponding to the type provided.
#
# Parameter
#   (Type) A string that is the symbol of the corresponding crypto currency I.E 'btc', 'eth', 'ada' , etc
def get_param(type):
    if type == 'btc':
        btc_param = {
            "slug": "bitcoin",
            "convert": "USD"
        }
        return btc_param
    elif type == 'eth':
        eth_param = {
            "slug": "ethereum",
            "convert": "USD"
        }
        return eth_param
    elif type == 'ada':
        ada_param = {
            "slug": "cardano",
            "convert": "USD"
        }
        return ada_param
    elif type == 'xrp':
        xrp_param = {
            "slug": "ripple",
            "convert": "USD"
        }
        return xrp_param
    elif type == 'ltc':
        ltc_param = {
            "slug": "litecoin",
            "convert": "USD"
        }
        return ltc_param
    elif type == 'xlm':
        xlm_param = {
            "slug": "stellar",
            "convert": "USD"
        }
        return xlm_param
    elif type == 'bnb':
        bnb_param = {
            "slug": "binance-coin",
            "convert": "USD"
        }
        return bnb_param
    elif type == 'doge':
        doge_param = {
            "slug": "dogecoin",
            "convert": "USD"
        }
        return doge_param
    elif type == 'usdt':
        usdt_param = {
            "slug": "tether",
            "convert": "USD"
        }
        return usdt_param


