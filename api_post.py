# 200: OK (successful request)
# 201: Created (resource successfully created)
# 400: Bad Request (client error)
# 401: Unauthorized (authentication failed)
# 404: Not Found (requested resource does not exist)
# 500: Internal Server Error (server error)

import requests

# Define the URL and payload data
url = 'https://jsonplaceholder.typicode.com/posts'
data = {
    'title': 'post',
    'body': 'request',
    'userId': 101
}

# Make a POST request with the data
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 201:
    print(f'Success! New post created with ID {response.json()["id"]}')
else:
    print(f'Error: {response.status_code}')