def Hello(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()    
        
Hello(3, "안녕하세요.", "hi", "hello")    
