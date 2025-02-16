# Write a program that takes a number as input and calculates the sum of all its digits.

def test01(nums):
    strng = str(nums)
    list_strC = list(strng)
    joinPlus = '+'.join(list_strC)
    
    
    qwe = eval(joinPlus)
    
    print(qwe)


# test01(123)



#Using sum 

def test02(nums):
    hold = 0
    strs = str(nums)

    for i in strs:
        hold += int(i)
        
    print(hold)


# test02(123)
