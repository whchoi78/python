def b(n):
    print("나는 b")
    return n*10

def a2(n1, n2, n3):
    print("나는 a")
    return n1*n2*b(n3)

print(a2(1, 2, 3))