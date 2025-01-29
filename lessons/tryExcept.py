# Try except is like try catch

try:
    user = int(input("Let us divide 10 with? "))
    output = 10/user
    print(float(output))

except:
    print("Math error")