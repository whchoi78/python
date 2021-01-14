
def func1():
    global var  #전역변수 선언
    var = 10
    print(var)

def func2():
    print(var)

var = 100 #전역변수 선언    
func1()
func2()