#Find longest diagonal return area, if multiple diagonal return highest area.
import math
def calDia(l,w):
    return round(math.sqrt(l**2 + w**2),2)

def calArea(l,w):
    return round((l * w),2)

def max_area():
    n = int(input("Enter the number of rectangles: "))
    max_diag = 0
    max_area = 0
    
    for i in range(n):
        # This is like destructuring [1,2], map is to make it integer so no need for longer for loop
        # map(function, iteration) = so doing this map(int, input), int is the function to make them int
        # using length, width = auto destructure or unpack it, if you want to list it just use single and add list() functions
        
        length, width= map(int, input(f"Enter length and width for rectangle {i+1}: ").split())
        x = calDia(length, width)
        y = calArea(length, width)
        
        
        # REMINDER GOAL: Find highest dia and return its area, if multiple dia just return dia with highest area
        # (1) Check if currentDia is bigger than max === if yes update the max dia and area 
        # (2) OR if equal ung currentDia and maxDia AND currentArea is bigger than maxArea === yes update the max dia and area 
        # With this ma prioritize si (1) and next is (2)
        
        if x > max_diag or (x == max_diag and y > max_area):
            max_diag = x
            max_area = y
        
    return f"The are of rectangle with the longest diagonal is: {max_area}"
         
print(max_area())