import requests

endpoint = "http://localhost:8000/api/products/1/"


get_response = requests.get(endpoint) # HTTP Request
# print(get_response.text) # Print raw text response
print(get_response.status_code)
print(get_response.json()) # JSON response