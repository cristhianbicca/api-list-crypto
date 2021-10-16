import requests



def get_response(api_url, crypto_coin, method):  
  if method == "ticker":
      response = get_ticker(api_url, crypto_coin, method)      
  elif method == "orderbook":
      response = get_orderbook(api_url, crypto_coin, method)
  elif method == "trades":
      response = get_trades(api_url, crypto_coin, method)
  else:
      return {"Method Invalid!"}

  return response

def connect_api(api_url, crypto_coin, method):  
  response = requests.get(api_url + crypto_coin + "/" + method)    
  try:
    response.raise_for_status()
  except requests.exceptions.HTTPError as e:    
    if "404" in str(e):
        return {"Coin not found!"}
    else:
        return "Error: " + str(e)
  return response.json()

def get_ticker(api_url, crypto_coin, method):
  ticker = connect_api(api_url, crypto_coin, method)    
  return ticker

def get_orderbook(api_url, crypto_coin, method):
  orderbook = connect_api(api_url, crypto_coin, method)      
  return orderbook

def get_trades(api_url, crypto_coin, method):
  trades = connect_api(api_url, crypto_coin, method)    
  return trades