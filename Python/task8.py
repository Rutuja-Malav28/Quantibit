# Extract email addresses from a text file. 
# Input (file content): 
# Contact us at support@example.com or admin@example.org. 
# Output: ['support@example.com', 'admin@example.org']

import re

def read_email_from_file(file_path):
    
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    try :
        with open(file_path,"r") as file:
            file_content = file.read()
            
            emails = re.findall(email_pattern, file_content)
            
            return emails
        
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
        return []
    

file_path = 'example.txt'  
emails = read_email_from_file(file_path)

print(emails)