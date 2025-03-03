# User input N, N of integers, then provide how many are higher than them
def test01():
    user = int(input("Input here: "))
    userList = input("Provide numbers: ").split()
    
    if len(userList) > user or len(userList) < user:
        return False
    
    appendInts = []
    
    for i in userList:
        appendInts.append(int(i))
    
    result = []
    
    for i in appendInts:
        count = 0
        for j in appendInts:
            if j > i:
                count += 1
        # If you put this inside the if statement of "j", everytime it meet the req, it will append.
        result.append(count)
    

    return result
print(test01())


'''
What will happen if we put it INSIDE?
10 9 8 > 10 = FALSE all append wont happen
10 9 8 > 9 = ONLY one so it will happen 1 time
10 9 8 > 8 = TWICE which are 1 and 2, why 2? becuase the count is stored in the "i" outside, so it will store the prev becuase same index
'''