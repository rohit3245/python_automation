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
    
    
    
