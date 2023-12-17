import requests
import json

data = {
    'area': 7420,
    'bedrooms': 4,
    'bathrooms': 2,
    'stories': 3,
    'mainroad': 1,
    'guestroom': 0,
    'basement': 0,
    'hotwaterheating': 0,
    'airconditioning': 1,
    'parking': 2,
    'prefarea': 1,
    'semi-furnished': False,
    'unfurnished': False,
}

url = 'http://0.0.0.0:9696/predict'

response = requests.post(url, json=data)
result = response.json()
print(json.dumps(result, indent=1))
