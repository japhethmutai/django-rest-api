import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "Learn the hard way!",
    "price": 32.99
}

get_response = requests.post(endpoint, json=data) # HTTP Request
# print(get_response.text) # Print raw text response
print(get_response.status_code)
print(get_response.json()) # JSON response