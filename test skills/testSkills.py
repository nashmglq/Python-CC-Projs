'''
“FizzBuzz” if i is divisible by 3 and 5,
“Fizz” if i is divisible by 3,
“Buzz” if i is divisible by 5
“i” as a string, if none of the conditions are true.

'''

user = int(input("Input a number: "))
empty = []
initial = 0

for i in range(0, user):
    initial += 1

    if initial % 3 == 0 and initial % 5 == 0:
        empty.append("FizzBuzz")

    elif initial % 3 == 0:
        empty.append("Fizz")

    elif initial % 5 == 0:
        empty.append("Buzz")
    else:
        empty.append(initial)

print(empty)
    

# use empty list, then push each value of loop and push it to the list