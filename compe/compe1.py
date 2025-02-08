'''
A E I O U
Write a program that counts the number of vowels in a given string.
'''


user = input("Enter a string: ").lower()
list_vowels = []
list_string = list(user)

for i in list_string:
    # check 1 by 1, is "a" in? yes append that iteration (which is a)
    if i in "aeiou":
        list_vowels.append(i)


print(len(list_vowels))
