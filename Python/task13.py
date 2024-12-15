# Implement the binary search algorithm. 
# Input: arr = [1, 3, 5, 7, 9], target = 7 
# Output: Found at index 3 

def binary_search(arr,target):
    low =0
    high = len(arr)-1
    
    while low <= high :
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return f"Found at index {mid}"
        
        elif arr[mid] > target :
            high = mid - 1
            
        else:
            low = mid + 1
            
    return "Not found"

arr = [1,3,5,7,9]
target = 7
result = binary_search(arr,target)
print(result)