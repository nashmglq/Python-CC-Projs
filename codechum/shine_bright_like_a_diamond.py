def shine_bright_like_a_diamond():
    n = int(input("Input here: "))
    
    
    if n % 2 == 0:
        n+=1
        for i in range(1, n+1, 2):
            calc = (n-i)//2
            if calc == 0:
                print("*" * (i//2), (n-1), "*" * (i//2))
            else:
                print(" " * calc, "*" * i)
                
        for i in range(n-2, 0, -2):
            calc = (n-i)//2
            print(" " * calc, "*" * i)
        
        

    else: 
        for i in range(1, n+1, 2):
            calc = (n-i)//2
            if calc == 0:
                print("*" * (i//2), n, "*" * (i//2))
            else:
                print(" " * calc, "*" * i)
                
        for i in range(n-2, 0, -2):
            calc = (n-i)//2
            print(" " * calc, "*" * i)
            

shine_bright_like_a_diamond()