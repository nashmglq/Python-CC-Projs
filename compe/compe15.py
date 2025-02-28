# Find the largest Number in the array
# float('-inf'), we make the 'inf' or smallest number as float
# So float('-inf') is the smallest number of ALL so we just compare it each time then we take it if it is greater than everthing
# If it is not then it wont store it to the max_number
def test01(arr):
    max_number = float('-inf')
    
    for i in arr:
        if i > max_number:
            max_number = i
            
    return max_number

print(test01([2,2,31,1,41,12]))