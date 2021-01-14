def Hello(value, n):
    for i in range(n):
            print(value)

Hello("안녕하세요", 3)            

def Gugudan(n):
    for i in range(n):
        print("10*{}={}".format(i,10*i))

Gugudan(10)

def Sum(start, end):
    total=0
    for i in range(start, end+1):
        total=total+i
    return total
    
print(Sum(1, 10))
print(Sum(5, 6))