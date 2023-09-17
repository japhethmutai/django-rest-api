import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "Learn simply",
    "content": "Learning Django rest framework is really easy",
    "price": 44.99
}

get_response = requests.post(endpoint, json=data) # HTTP Request
# print(get_response.text) # Print raw text response
print(get_response.status_code)
print(get_response.json()) # JSON response