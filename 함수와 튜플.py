'''
def func():
    return 10, 20

a, b = func()
print(a)
print(b)    
'''

def Func(f):
    for i in range(10):
        f()

def Print():
    print("hello oncourse")

Func(Print)    
'''
#map(), filter()

def func1(n):
    return n+10

def func2(n):
    return n<3

ls = [1, 2, 3, 4, 5] 
ls2 = map(func1, ls)
print(list(ls2))


ls3 = filter(func2, ls)
print(list(ls3))
'''