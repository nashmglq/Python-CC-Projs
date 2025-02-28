# Get highest dia, if same value provide the area (py theorem)
import math
def test01():
    user = int(input("Enter the number of rectangle "))
    appendHere = []
    appendDiagonal = []
    
    for i in range(user):
        userNew = input(f"Enter the length and width for the rectangle {i+1}: ").split()
        if len(userNew) > 2:
            return False
        else:
            appendHere.append(userNew)
        
    for j in range(len(appendHere)): 
        # FOUND THE PROBLEM using "i" instead of "j"
        x = appendHere[j]
        for i in range(len(x)-1):
            y = round((math.sqrt((int(x[i]))**2 + (int(x[i+1]))**2 )), 2)
            appendDiagonal.append(y)
           
    # Now let us sort     
    for k in range(len(appendDiagonal)):
        for p in range(len(appendDiagonal)-k-1):
            if appendDiagonal[p] > appendDiagonal[p+1]:
                appendDiagonal[p], appendDiagonal[p+1] = appendDiagonal[p+1], appendDiagonal[p]
                
                
    # if 

print(test01())
