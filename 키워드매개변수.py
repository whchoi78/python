'''
def Hello(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()    
        
Hello("안녕하세요.", "hi", "hello", n=3)    
'''
'''
def Hello(a=1, b=2, c=3):
    print(a, b, c)

Hello(100, 200, 300)
Hello(a=100, b=200, c=300)
Hello(c=100, b=200, a=300)
Hello(100, c=300)
'''

def hello(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

hello("안녕하세요", "헬로우", "봉주르")  #인사말 두 번
hello("안녕하세요", "헬로우", "봉주르", n=3)  #인사말 세 번
hello("안녕하세요", "헬로우", "봉주르", n=4)  #인사말 네 번