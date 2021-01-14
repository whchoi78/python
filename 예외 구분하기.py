ls = [3, 7, 1, 5, 4]

try:
    idx = int(input("인덱스 입력: "))
    print("{}번째 요소 : {}".format(idx, ls[idx]))
    #예외.발생()

except ValueError as exception:
    print("정수를 입력하세요")
    print(exception)

except IndexError as exception:
    print("리스트의 인덱스를 벗어났습니다.") 
    print(exception)
except Exception as exception:
    print("예기치 못한 예외가 발생했습니다.")
    print(exception)      