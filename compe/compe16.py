# Find the second largest number


# This is a bad code, it will only remove the first occurance. It also have 2 loops
def test01(arr):
    max1 = max2 = float('-inf')
    arr.sort()


    for i in arr:
        if i > max1:
            max1 = i
    arr.remove(max1)
    
    for i in arr:
        if i > max2:
            max2 = i
            
    return max2
    
# This is a better code


def test02(arr):
    max1 = max2 = float('-inf')
    
    for i in arr:
        if i > max1:
            max1 = i
            # So get the highest pero dapat lower sya sa max1
            if i > max2 and i < max1:
                max2 = i

test02([1,2,3,41,12,323,1])



'''
def test01(ints):
    toStrs = str(ints)

    if toStrs == toStrs[::-1]:
        return f"{toStrs} reads as {toStrs} from left to right and from right to left."
    else:
        return f"From left to right, it reads {toStrs}. From right to left, it becomes {toStrs}. Therefore it is not a palindrome."

print(test01(121))

'''