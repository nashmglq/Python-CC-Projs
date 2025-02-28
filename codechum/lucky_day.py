#Print the days, to be lucky

def test01():
    numberOfDays = int(input("Enter the number of days: "))
    oddsOfDays = input("Enter the odds of luck for each day: ").split()
    emptyBigger = []
    
    if len(oddsOfDays) > numberOfDays:
        print("Invalid")
        
    #Check if next is bigger than the prev
        
    for j in range(len(oddsOfDays)-1):
        if oddsOfDays[j+1] > oddsOfDays[j]:
            
            x = int(oddsOfDays[j+1]) - int(oddsOfDays[j])
            emptyBigger.append(x)
            
        else:
            emptyBigger.append('0')

    return emptyBigger
print(test01())