# Turn strings = "One hunderd thousand"
# Into int = 100000


number_words = {
    # Basic numbers
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19,

    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90,


    "hundred": 100, "thousand": 1000
}


def hundreds(str):
    multiplyHundreds = number_words[str]
    return multiplyHundreds

def thousands(str):
    multiplyThousands = number_words[str]
    return multiplyThousands

def dashRemover(rmv):
    dashRemover = rmv[0].split("-")
    firstNum = dashRemover[0]
    secondNum = dashRemover[1]
    output = number_words[firstNum] + number_words[secondNum]
    return output

def dashChecker(chk):
    initialValue = chk[0]
    dashChecker = "-" in chk[0]
    
    if dashChecker == True:
        remover = dashRemover(chk)
        return remover
    
    return number_words[initialValue]

    

def converter(str):
    try: 
        initialSpace = str.split(" ")
        if len(initialSpace) == 2:
            doubleNewValue = dashChecker(initialSpace)
            if initialSpace[0] == "hundred":
                hundredsMultiplier = hundreds(initialSpace[1])
                print(doubleNewValue * hundredsMultiplier)
            else:
                thousandsMultiplier = thousands(initialSpace[1])
                print(doubleNewValue * thousandsMultiplier)
            
            
        elif len(initialSpace) == 3:
            quadNewValue = dashChecker(initialSpace)
            hundredsMultiplier = hundreds(initialSpace[1])
            thousandsMultiplier = thousands(initialSpace[2])
            print(quadNewValue * hundredsMultiplier * thousandsMultiplier)  
        
            
        else:
            singleValue = dashRemover(initialSpace)
            print(singleValue)

    except Exception as error:
        print(error)
    
    
converter("one hundred thousand")
# dashChecker("forty-six")






