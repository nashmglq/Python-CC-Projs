'''
Create a palindrome checker
'''
import re


user = input("Check Palindrome: ")

space_removed = user.replace(" ", '')
# Corrected regex pattern to remove special characters
# removing_spe_char = re.sub(r"[,'._():\/\\\-]", "", space_removed)
list_input = list(user.replace(" ", ''))
getReversed = []
output = ''.join(list_input)

for i in reversed(list_input):
    getReversed.append(i)
    

if getReversed == list_input:
    print("Palindrome, here is your input & reversed: ", list_input, getReversed, list_input[::-1] )