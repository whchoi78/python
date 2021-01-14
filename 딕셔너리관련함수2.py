dic = {1:"일", 2:"이", 3:"삼"}
dic2 = {5:"오", 6:"육"}

dic.setdefault(3, "삼") #키가 없다면 추가
print(dic)

dic.update(dic2) #다른 사전의 내용을 추가
print(dic)

dic.pop(6)   #키에 해당하는 값을 삭제
print(dic)

dic.clear()   #딕셔너리 항목 모두 삭제
print(dic)