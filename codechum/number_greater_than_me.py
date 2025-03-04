# Count the number greater than me
# [1,2,3] = [2,1,0]

def num_greater_than_me():
    n = int(input("Enter the number of integers: "))
    nums = list(map(int, input(f"Enter {n} intergers: ").split()))
    
    if n != len(nums):
        return False
    
    results = []
    
    for i in range(n):
        count = 0
        
        for j in range(n):
            if nums[j] > nums[i]:
                count+=1
                
        results.append(count)
    return results


print(num_greater_than_me())