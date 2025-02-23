# String Capitalization: Write a function called capitalize_even_letters that takes a string and 
# returns a new string with all characters at even indices capitalized.


def test01(strs):
    list_strs = list(strs)
    appendHere = []
    
    for i in range(0, len(list_strs)):
        if i % 2 == 0:
            appendHere.append(list_strs[i].upper())
        else:
            appendHere.append(list_strs[i])
            
    print("".join(appendHere))
    
    
    
test01("hello world")