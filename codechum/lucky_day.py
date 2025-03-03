
def luckyDay():
    n = int(input("Enter the number of days: "))
    days = list(map(int, input("Enter the odds of luck for each day: ").split()))

    if n  != len(days):
        return False
    
    result = []
    
    for i in range(len(days)):
        #Reset each iteration of "i"
        count = 0
        #To get the next index of "j" loop
        for j in range(i+1, len(days)):
            count += 1
            
            if days[j] > days[i]:
                result.append(count)
                break
        # Run outside so if days[j] !> days[i] it wont append each iteration of j
        # The else is connected to "j" if "j" break the iteration of "i" break, else append 0
        
        else:
            result.append(0)

        
    return result
            
print(luckyDay())