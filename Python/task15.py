# Refactor poorly written code. 
# Input (unoptimized code): 
 
# def unoptimized_code(numbers): 
#     result = "" 
 
#     for num in numbers: 
#         if num % 2 == 0: 
#             square = num * num   
#             result += f"Square of {num} is {square}\n"                               
#     max_num = -1 
#     for num in numbers: 
#         if num > max_num: 
#             max_num = num 
 
#     count_dict = {} 
#     for num in numbers: 
#         if num in count_dict: 
#             count_dict[num] += 1 
#         else: 
#             count_dict[num] = 1 
 
#     result += f"\nMax number is {max_num}\n" 
#     result += "Number counts:\n" 
#     for num, count in count_dict.items(): 
#         result += f"{num}: {count}\n" 
 
#     return result 
 
# Output:(Optimised Code)


from collections import Counter

def optimized_code(numbers):
    squares = [f"Square of {num} is {num * num}" for num in numbers if num % 2 == 0]
    
    max_num = max(numbers) if numbers else None
    
    count_dict = Counter(numbers)
    
    result = []
    result.extend(squares)
    result.append(f"\nMax number is {max_num}\n")
    result.append("Number counts:\n")
    

    for num, count in count_dict.items():
        result.append(f"{num}: {count}")
    

    return '\n'.join(result)


numbers = [1, 2, 2, 3, 4, 4, 4, 5]
print(optimized_code(numbers))
