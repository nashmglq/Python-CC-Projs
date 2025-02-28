# Add or Subtract 1 then check if divisble by 3

def test01():
    user = int(input("Input: "))
    listOfUser = []
    appendHere = []

    for i in range(user):
        userList = input("Input: ")
        listOfUser.append(userList)
        
    for i in listOfUser:
        x = int(i)
        
        if (x-1) % 3 == 0:
            appendHere.append(x)
        elif (x+1) % 3 == 0:
            appendHere.append(x)
        else:
            None
        
    return len(appendHere)
    
print(test01())