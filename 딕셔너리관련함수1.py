dic = {1:"일", 2:"이", 3:"삼"}

print(dic.keys()) # 모든 키 반환
print(dic.values()) # 모든 값 반환
print(dic.items()) # 모든 키, 값 반환

for key in dic.keys():
    print(key, end=" ")
print()   

for values in dic.values():
    print(values, end=" ")
print()
for key, values in dic.items():
    print(key,":",values, end=" ")   
print()    