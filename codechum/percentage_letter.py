# Find the percentage of the char in string.
def test01():
    userSentence = input("Enter a string: ")
    userChar = input("Enter a char: ")
    x = len(userSentence)
    y = []
    
    for i in userSentence:
        if i in userChar:
            y.append(i)
            
    # (gustoMo / basis) * 100 
    calcu = int((len(y)/x) * 100)
    return f"{calcu}%"

print(test01())