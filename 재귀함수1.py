def Recursive(n):
    if n == 0:
        return
    print("재귀함수 입니다.")
    Recursive(n-1)

Recursive(3)