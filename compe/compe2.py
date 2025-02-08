'''
Write a Python program that takes an integer n as input and prints a list of the odd numbers between 0 and n (inclusive).
'''
user = int(input("Insert Integer: "))

odd = []

for i in range(0, user+1):
    if i % 2 == 1:
        odd.append(i)
    
    

print(odd)

