import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "Hello World is now Django!",
    "price": 3.33
}

get_response = requests.put(endpoint, json=data) # HTTP Request
# print(get_response.text) # Print raw text response
print(get_response.status_code)
print(get_response.json()) # JSON response