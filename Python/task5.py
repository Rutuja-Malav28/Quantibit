# Validate user input as an integer. 
# Input: "abc" 
# Output: Invalid input. Please enter a number. 
# Input: "123" 
# Output: You entered: 123

def validate_input(user_input):
    try:
        number = int(user_input)
        print("You entered: ",number)
    
    except ValueError:
        print("Invalid input. Please enter a number.")
        
user_input = input("Enter input: ")

validate_input(user_input)