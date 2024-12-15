# Find the second largest number in a list. 
# Input: [10, 20, 4, 45, 99] 
# Output: 45 

list1 = [10, 20, 4, 45, 99]

max1 = 0
max2 = 0

for i in list1:
    if i > max1: 
        max2 = max1  
        max1 = i  
    elif i > max2 and i != max1: 
        max2 = i 

print("Therefore the second largest number is:", max2)