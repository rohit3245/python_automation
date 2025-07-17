# 200: OK (successful request)
# 201: Created (resource successfully created)
# 400: Bad Request (client error)
# 401: Unauthorized (authentication failed)
# 404: Not Found (requested resource does not exist)
# 500: Internal Server Error (server error)

import requests

#Define the URL and Updated Data

url = 'https://jsonplaceholder.typicode.com/posts/1'
data = {
    'title' : 'updated title',
    'body' : 'updated body',

}

#make put request to update resource

response = requests.put(url, json=data)

#Check if the request is successful 

if response.status_code == 200:
    print(f'Success.. post updated: {response.json()}')
else:
    print(f'Error!! : {response.status_code}')
    


#make a request to delete resource

response = requests.delete(url)

#Check if the request is successful 

if response.status_code == 200:
    print('Success.. post deleted')
else:
    print(f'Error!! : {response.status_code}')