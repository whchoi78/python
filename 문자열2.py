st = "파이썬꿀잼"

#문자열 각 요소 접근
print(st[0], st[1], st[2])

#문자열 슬라이싱
print(st[0:3])

#문자열 각 요소 츨력
for i in range(len(st)):
    print(st[i],end="")
print()

for i in st:
    print(i, end="")