'''
Rows will depend on the user input
*
**
***
****
'''


user = int(input("How many rows: "))

for i in range(0, user):
    #Multiply to each "i" or iterations
    print("*" * (i+1))