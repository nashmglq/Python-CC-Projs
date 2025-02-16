#isalnum() = return true if all are numec or alpah, false if not hehe

def test01(strs):
    lowerCase = strs.lower()
    list_of_str = list(lowerCase)
    appendHere = []
    
    for i in list_of_str:
        qwe = i.isalnum()
        if qwe:
            appendHere.append(i)
    
    if appendHere[::-1] == appendHere:
        print("A palindrome")
        
    else:
        print(f"Not a palindrome Initial Input: {appendHere}", appendHere[::-1])
    
    
# test01("A man, a plan, a canal: Panama!")

#USING STRING AS AN APPEND

def test02(strs):
    lowerCase = strs.lower()
    appendString = ""
    
    for i in lowerCase:
        # Sorry for the var name hihi, but this is to append if it is (isal or num)
        qwe = i.isalnum() 
        
        if qwe:
            #Append the i, because if qwe returns true to checking, it will append that iteration
            appendString += i

            
    if appendString[::-1] == appendString:
        print("Palindrome")
        
    else:
        print("Not a palindrome")    


test02("A man, a plan, a canal: Panama!")

