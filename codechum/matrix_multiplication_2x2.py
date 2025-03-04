
def matrix():
    appendMatrix1 = []
    appendMatrix2 = []
    results = []
    finalResult = []
    
    for i in range(2):
        matrix1 = list(map(int, input(f"Enter row and column for matrix 1: ").split()))
        appendMatrix1.append(matrix1)
        
    for i in range(2):
        matrix2 = list(map(int, input("Enter row and column for matrix 2: ").split()))
        appendMatrix2.append(matrix2)
        
    '''
    SOLVING MATRIX:
    Take the first row.
    Multiply each number in the row with the matching number in the first column.
    Add up the results.
    Move to the next column and do the same.
    Repeat for the second row.
    '''
    
    
    for i in range(len(appendMatrix1)):
        row1 = appendMatrix1[i]
        indexR1 = row1[0]
        indexR2 = row1[1]
        

        for j in range(len(appendMatrix2)):
            col1 = appendMatrix2[j]
            col2 = appendMatrix2[j-1]
            indexC1 = col1[j]
            indexC2 = col2[j]
            
            if j != 0 : 
                matrix1Result = indexR1*indexC2 + indexR2*indexC1
            else:
                matrix1Result = indexR1*indexC1 + indexR2*indexC2
            results.append(matrix1Result)
            
                
    final = list(map(int, results))
    finalResult.append([final[0], final[1]])
    finalResult.append([final[2], final[3]])  

    return finalResult

print(matrix())
