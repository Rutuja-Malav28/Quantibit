# Parse a JSON file and print keys and values. 
# Input (JSON file): 
# { 
# } 
# "name": "Alice", 
# "age": 30, 
# "city": "Wonderland" 
# Output: 
# name: Alice 
# age: 30 
# city: Wonderland 

import json 

def prase_json_file(file_path):
    
    with open(file_path,"r") as file:
        
        data = json.load(file)
        
    for key, value in data.items():
        print(f"{key} : {value}")
        
file_path ="data.json"

prase_json_file(file_path)
            
        