import requests

endpoint = "http://localhost:8000/api/auth/"

get_response = requests.post(endpoint) # HTTP Request
print(get_response.json()) # JSON response

endpoint = "http://localhost:8000/api/products/"

get_response = requests.get(endpoint) # HTTP Request
print(get_response.status_code)
print(get_response.json()) # JSON response