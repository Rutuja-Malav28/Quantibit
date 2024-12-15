# Read a file containing integers and calculate their sum. 
# Input (file content): 
# 12 
# 15 
# 8 
# 23

def sum_of_int(file_name):
    total_sum =0
    with open(file_name,'r') as file:
        for i in file:
            total_sum += int(i.strip())
            
    return total_sum

file_name ="numbers.txt"
print("The total sum of integers in the file is : " , sum_of_int(file_name))


# The total sum of integers in the file is :  58