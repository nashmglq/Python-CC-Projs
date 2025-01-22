user_input = int(input("Insert number:"))

if((user_input % 2) == 0 and user_input >= 2 and user_input <= 5):
    print("Not Weird")

elif((user_input % 2) == 1):
    print("Weird")
    
elif((user_input % 2) == 0 and user_input >= 6 and user_input <= 20):
    print("Not Weird")
    
elif((user_input % 2) == 0 and user_input > 20):
    print("Not Weird")
else:
    print("Something wrong")