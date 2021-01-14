import random

lotto = []

while True:
    num = random.randrange(1, 47)
    if lotto.count(num) == 0 :
        lotto.append(num)
    if len(lotto) == 6:
        break
print("추첨된 번호 : ", end="")
lotto.sort()

for i in range(len(lotto)):
    print("{} ".format(lotto[i]), end="")
print()

while True :
    num = random.randrange(1, 47)
    if lotto.count(num) == 0:
        lotto.append(num)
    if len(lotto)==7:
        break
print("보너스 번호: {}".format(lotto[6]))        