# Fetch data from a public API and display it. 
# Input: Call an API like https://jsonplaceholder.typicode.com/posts/1 
# Output: 
# { 
# } 
# "userId": 1, 
# "id": 1, 
# "title": "sunt aut facere repellat provident occaecati", 
# "body": "quia et suscipit suscipit recusandae"
# }

import requests

def call_user_api():
    
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        
        data =response.json()
        
        print(data)
        
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

call_user_api()
