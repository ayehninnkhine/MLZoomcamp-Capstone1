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

url = 'https://housing-3zktkdeu6a-uc.a.run.app/predict' #Google Cloud Deployment

response = requests.post(url, json=data)
result = response.json()
print(json.dumps(result, indent=1))
