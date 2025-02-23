# Functions in python

'''
def my_addition_func(num1, num2):
    sum = num1 + num2
    print(sum)


my_addition_func(5,7)
'''

# *args and **kwargs


# "*" unpacking (like destructuring in javascript)
# this will put it into a tupple
# "**" same function
# However, it will use put it into a dictionary (objects)

# * is for unpacking tuples or lists (positional arguments).
# ** is for unpacking key-value pairs (dictionaries).

# def myFunc(parameter)
# myFunc(arguements)





def order_pizza(size, *topings, **details):
    print(f"Ordering a {size} pizza with a topping of: ")
    for x in topings:
        print(x)
    for y in details:
        print(y)    

# Size is matched to the first parameter; toppings are collected as the second until a key-value pair is encountered.        
order_pizza("large", "sausage", "cheese", delivery=True, tip=10)



