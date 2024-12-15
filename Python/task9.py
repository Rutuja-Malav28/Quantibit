# Calculate mean, median, and mode of a dataset. 
# Input: [1, 2, 2, 3, 4] 
# Output: 
# Mean: 2.4 
# Median: 2 
# Mode: 2

import statistics

def calculate(data):
    
    mean = statistics.mean(data)
    
    median = statistics.median(data)
    
    try:
        mode = statistics.mode(data)
        
    except statistics.StatisticsError:
        mode = "No unique mode"
        
    print(f"Mean: {mean}")
    print(f"Medain: {median}")
    print(f"Mode: {mode}")
    
data = [1, 2, 2, 3, 4]

calculate(data)