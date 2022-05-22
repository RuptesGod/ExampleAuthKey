import requests
import json

key = input('Enter your key: ')

keys = requests.get('YOUR RAW LINK')

if keys.status_code == 200:
    jr = keys.json()
    values = jr.values()
    if key in values:
    	print("Success!")
    else:
    	print("Error")
elif keys.status_code == 404:
    print("No connect")

