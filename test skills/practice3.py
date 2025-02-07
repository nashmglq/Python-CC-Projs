# Create a Palindrome 
user = input("Check Palindrome: ").lower()
list_char = list(user.replace(" ", ""))
reverse = list_char[::-1]
x = ''.join(reverse)
y = ''.join(list_char)

'''
OR
for i in reversed(list_char):
    print(i)

Then append
'''


if y == x:
    print(f"{user} is a palindrome")
else:
    print("Not a palindrome")

