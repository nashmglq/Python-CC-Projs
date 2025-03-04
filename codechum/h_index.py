
def h_index():
    n = int(input("Enter the number of papers: "))
    citations = list(map(int, input("Enter the number of citations for each paper: ").split()))

    for i in range(n):
        
       for j in range(n-1-i):
           if citations[j] < citations[j+1]:
               citations[j], citations[j+1] = citations[j+1], citations[j] 
    
    count = 0
    
    for i in range(1, n):
        if citations[i] > i:
            count+=1
            
    return count,citations
            



print(h_index())