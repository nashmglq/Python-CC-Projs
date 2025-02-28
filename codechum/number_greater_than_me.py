# User input N, N of integers, then provide how many is the diff from them to the highest

def test01():
    user = int(input("Input here: "))
    userList = input("Provide numbers: ").split()
    
    if len(userList) > user or len(userList) < user:
        return False
    
    maxNumber = max(userList)
    appendAnswers = []
    for i in userList:
        y = int(maxNumber) - int(i)
        appendAnswers.append(y)
    return appendAnswers

print(test01())