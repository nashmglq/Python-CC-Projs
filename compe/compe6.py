# Write a program that takes a word or sentence and a letter as input, then checks if the letter exists, counts its occurrences,
# and finds its positions in the text.

user = input("Provide a sentence: ")
find = input("What letter to find:  ")
len_checker = len(list(find))
len_counter = []


if len_checker > 1:
    print("One letter only pls")
    

for i in user:
    if i in find:
        len_counter.append(i)


if len(len_counter) > 1:
    print(len(len_counter))
    
else: 
    print("Not found")

