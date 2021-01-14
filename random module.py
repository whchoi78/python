import random

#0.0 ~ 1.0 사이의 임의의 실수를 반환
print(random.random())

#지정한 범위 사이의 임의의 실수 반환
print(random.uniform(2, 3))

#리스트의 요소를 랜덤하게 선택
print(random.choice(["하나", "둘", "셋"]))

#지정한 범위의 정수를 반환
print(random.randrange(10, 15))

#리스트를 임의로 섞음
ls=[1,2,3,4,5]
random.shuffle(ls)
print(ls)

#리스트의 요소 중에 k개를 뽑음
print(random.sample([1,2,3,4,5], k=2))