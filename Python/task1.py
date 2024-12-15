# Reverse a string without using built-in methods.
# Input: "hello"
# Output: "olleh"

str = "hello"
reversed_str = ""

for i in str:
    reversed_str = i + reversed_str
    
print("Output string is : " + reversed_str)


# Output string is : olleh