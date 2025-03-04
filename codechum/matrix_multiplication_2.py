

def matrixDimensions():
    while True:
        a, b = map(int, input("Matrix 1: ").split())
        c, d = map(int, input("Matrix 2: ").split())
        
        if b != c:
            print("Invalid Dimensions")
            continue
        
        matrixCalculations(a,b,c,d)
        break
        
    
    return(matrixCalculations(a,b,c,d))
        

def matrixCalculations(a,b,c,d):
    appendMatrix1 = []
    appendMatrix2 = []


    for i in range(a):
        matrix1 = list(map(int, input(f"Enter element of Matrix1 {a}x{b}: ").split()))
        appendMatrix1.append(matrix1)    
        
    for i in range(d):
        matrix2 = list(map(int, input(f"Enter element of Matrix2 {c}x{d}: ").split()))
        appendMatrix2.append(matrix2)   
    
    if len(appendMatrix1) != a or len(appendMatrix2) != c:
        print("Invalid Matrix Inputs")

    result = []
    
    
    #Initializing RESULT TO APPEND EASIER
    #Range of "a" to check rows
    for i in range(a):
        row = []
        #Range of "d" to get col
        for j in range(d):
            row.append(0)
        result.append(row)
    #REMEMBER TO GET THE DIMENSION WE NEED THE A AND D

    for i in range(a):  
        for j in range(d):  
            for k in range(b):  
                result[i][j] += appendMatrix1[i][k] * appendMatrix2[k][j]
    
    '''
    EXAMPLE LOGIC TO UNDERSTAND
    i = 0 j =0 k = 0
    result[0][0] += appendMatrix1[0][0] * appendMatrix2[0][0]
    matrix1 = [[1,2],[3,4]]
    matrix2 = [[5,6],[7,8]]
    result = [[0,0], [0,0]]
    [0] += 1*5  results = 5
    
    i = 0 j =0 k = 1
    result[0][0] += appendMatrix1[0][1] * appendMatrix2[1][0]
    matrix1 = [[1,2],[3,4]]
    matrix2 = [[5,6],[7,8]]
    result = [[0,0], [0,0]]
    [0][0] = 5 += 2 * 7 = 19 
    '''
            
            
    return appendMatrix1, appendMatrix2



print(matrixCalculations(2,2,2,2))
# print(matrixDimensions()) 