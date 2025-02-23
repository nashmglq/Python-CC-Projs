# Remove Duplicate Characters: Implement a function that removes all duplicate characters from a string,
# preserving the order of the first occurrence of each character.

def test01(strs):
    appendHere = []
    for i in strs:
        if i in appendHere:
            None
        else:
            appendHere.append(i)

    print("".join(appendHere))        
        

test01("Heloo World?")