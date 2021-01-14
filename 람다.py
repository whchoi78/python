'''
def func1(n):
    return n+10

def func2(n):
    return n<3
'''

#func1 = lambda n : n+10
#func2 = lambda n : n<3

ls = [1, 2, 3, 4, 5] 
ls2 = map(lambda n : n+10, ls)
print(list(ls2))


ls3 = filter(lambda n : n<3, ls)
print(list(ls3))