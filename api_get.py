# 200: OK (successful request)
# 201: Created (resource successfully created)
# 400: Bad Request (client error)
# 401: Unauthorized (authentication failed)
# 404: Not Found (requested resource does not exist)
# 500: Internal Server Error (server error)


import requests

# make a GET request to URL
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Print the response content
    print(response.json())
else:
    # Print an error message
    print(f'Error: {response.status_code}')
    
    
    
