from vouched import config
import requests
import json

## function to get the data, and to return it
def request_api(path, method = 'POST', data=None, apiKey = config.get('API_KEY')):
  # merge url
  url = "{}{}".format(config.get('API_URL'),path)

  # add key
  headers = {
    'Content-Type': 'application/json',
    'X-Api-Key': apiKey
  }
  # stringified json
  if data:
    data = json.dumps(data)

  x = requests.request(method, url, headers=headers, data=data)
  o = json.loads(x.text)
  return o 


   

    
    
    