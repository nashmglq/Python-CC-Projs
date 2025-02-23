# Write a function that takes two strings as input and returns True if they are anagrams 
# (contain the same characters with the same frequency) and False otherwise.



#Own Version
def test01(strs1, strs2):
    x = strs1.lower()
    y = strs2.lower()
    res = ""
    for i in x:
        if len(x) == len(y):
            #This will work but the "in" is not a good practice, so use sorted hehe
            if i in y:
                res = "true"
        else: 
            res = "false"
    print(res)

       
       
test01("apple", "pale")


# Better version

def test02(strs1, strs2):
    if len(strs1) != len(strs2):
        return False

    return sorted(strs1.lower()) == sorted(strs2.lower())

print(test02("apple", "pale"))  


# Combine 

def test03(strs1,strs2):
    x = None
    if len(strs1) != len(strs2):
        x = False
    
    if sorted(strs1.lower()) == sorted(strs2.lower()):
        x =  True 

    print(x)

test03("silent", "listen")



