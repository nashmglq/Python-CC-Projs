# Get highest dia, if same value provide the area (py theorem)
import math
def test01():
    # USER INPUTS
    appendHere = []
    appendDiagonal = []
    appendDicts = {}
    user = int(input("Enter the number of rectangle "))
    for i in range(user):
        userNew = input(f"Enter the length and width for the rectangle {i+1}: ").split()
        if len(userNew) > 2:
            return False
        else:
            appendHere.append(userNew)
    
    # Calculation for diagonal
    for j in range(len(appendHere)): 
        # FOUND THE PROBLEM using "i" instead of "j"
        x = appendHere[j]
        for i in range(len(x)-1):
            y = round((math.sqrt((int(x[i]))**2 + (int(x[i+1]))**2 )), 2)
            appendDiagonal.append(y)
            appendDicts.update({y:x})
           
    # Bubble_Sort or we can use .sort() hehe
    for k in range(len(appendDiagonal)):
        for p in range(len(appendDiagonal)-k-1):
            if appendDiagonal[p] > appendDiagonal[p+1]:
                appendDiagonal[p], appendDiagonal[p+1] = appendDiagonal[p+1], appendDiagonal[p]
                
    # Check for the largest, if there are more than 1 get the w and l and get area



print(test01())
