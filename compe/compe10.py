# Create a function that removes all punctuation characters from a string.

def test01(strs):
    appendHere = []
    for i in strs:
        if i.isalnum():
            print(appendHere.append(i))
            
    x = "".join(appendHere)
    print(x)


test01("Hello, kamusta ka?")