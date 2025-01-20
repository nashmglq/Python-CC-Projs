# File handler in python


wow = open('./src/example.txt', 'r')


# Read file
print(wow.read())

# Print line by line
print(wow.readline(1), end="3")
print(wow.readline())

# Write into a file?
wew = open('./src/write.txt', 'w')
wew.write("Something new?")

#Append
# Write into a file?
wew = open('./src/write.txt', 'a')
wew.write(" \nSomething new?!")