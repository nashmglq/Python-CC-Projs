#Sort the user input:
# user = input("Input here: ").split()
# empty = []


def sorting(arr):
    # range(start, stop)
    
    # SO I SOLELY PURPOSE IS to make the checking of j smaller each time
    # the i will still be needed to iterate the range of the array
    for i in range(0, len(arr)): # Do this loop
        
        
        #Explaining len(arr)-i-1 =  each iteration i will make the range j smaller, so it wont check everthing.
        #(check everthing will still works but takes too mcuh time)
        # IN addition, -1 is needed because it will represent the +1 in the j
        
        for j in range(len(arr) - i - 1): #Finish this loop before loop i
            if arr[j] > arr[j+1]: #This is like saying "if prev index is greater than next index"
                arr[j], arr[j+1] = arr[j+1], arr[j] # SWAP THEM, THIS WILL AUTO CHANGE THE ARR SO JUST CALL IT
                
    
    return arr #ahh like saying "change this index to this value"
    

# sorting([3,2,1])



# print(sorting([3,2,1]))


user = input("Input your numbers: ").split()


for i in range(len(user)):
    for j in range(len(user)- 1):
        if user[j] > user[j+1]:
            user[j], user[j+1] = user[j+1], user[j]


print(user)

