# Reverse the INTEGER  N = RN = RRN = true if RRN = N
# REMEMBER 0 cannot be the starter of an integer, it will cause an error, so we just remove 0 from the input (if it is last and the prev is zero)

def test01():
    # We can remove the int already here
    user = int(input("Input: "))
    x = str(user)
    y = list(x)
    reverN = y[::-1]
    reverReverN = reverN[::-1]
    
    
    if y[-1] == '0':
        return False
    

    if reverReverN == y:
        return True


print(test01())