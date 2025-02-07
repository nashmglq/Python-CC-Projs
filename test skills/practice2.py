'''
A E I O U
Write a program that counts the number of vowels in a given string.
'''

user = input("Provide a string: ").lower()
test = list(user)
my_vowels = []

# if what is true, that will only be appended


# fetchVowels = [char for char in test if char in 'aeiou']
# print(len(fetchVowels))

# OR 
# if what is true, that will only be appended


for i in test:
    if i in 'aeiou':
        my_vowels.append(i)
print(len(my_vowels))




'''
fetchVowels = [char for char in test if char == 'a' or 'e' or 'i' or 'o' or 'u']
This won't work, it will only check the list has this letters and will append it if it matches even one of them


fetchVowels = [char for char in test if char in 'aeiou']
This work, because it will check each if it contains, it will be "or" and "and"

'''




