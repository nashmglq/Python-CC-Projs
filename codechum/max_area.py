# Find max diagonal and return area
# Multiple max diagonal, find the highest area then return it
import math


def pyTh(l,w):
    return round(math.sqrt(l**2 + w** 2),2)
def calArea(l, w):
    return round(l * w, 2)


def rectangle():
    n = int(input("Enter the number of rectangles: "))
    maxDiagonal = 0
    maxArea = 0
    
    for i in range(n):
        length, width = map(int, input(f"Enter the length and width of rectangle {i+1}: ").split())
        
        diagonal = pyTh(length, width)
        area = calArea(length, width)
    
        if diagonal > maxDiagonal:
            maxDiagonal = diagonal
            maxArea = area
       
        elif diagonal == maxDiagonal:
            if area > maxArea:
                # maxDiagonal = diagonal
                maxArea = area
    
    return f"The area of the rectangle with the longest diagonal is : {maxArea}"


print(rectangle())