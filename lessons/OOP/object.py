# Object in python
'''
Object is just like object in real life

It consist of:
Attributes = What an object is/has (name, age, height)
Methods = Actions (eat, sleep)

'''

# We will use class to create an Object
# Class is like a blueprint to describe what attributes and methods to do
# Use capital letters when using class

class Dog:

    # Constructor where we will input our attributes
    # __init__ means initialized
    def __init__(self,breed, smell, height):
      # Self represent the object currently being used
      self.breed = breed
      self.smell = smell
      self.height = height

    # self represents the object using this method (action)
    # so when we called "hepe" it will become the self (which is the one will represent it on the other file)
    def bark(self):
        # We can call attribute (in the init function) as long as it belongs to the same object
        print( self.breed + " is barking")

    def silence(self):
        print("This dog silenced")

# CONCLUSION: SELF IS THE ONE USING THE OBJECT HEHE