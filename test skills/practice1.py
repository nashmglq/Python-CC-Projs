'''
Write a Python program that takes an integer n as input and prints a list of the odd numbers between 0 and n (inclusive).
'''



n = int(input("Enter an integer: "))
arr_odd = []
arr_even = []

for i in range(0, n):
    
    #Filter every odd and push that
    if i % 2 == 1:
        arr_odd.append(i)
    elif i % 2 == 0:
        arr_even.append(i)

print(arr_odd)
print(arr_even)