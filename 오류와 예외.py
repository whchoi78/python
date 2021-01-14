try:
    age = int(input("나이를 입력하세요 : "))
except:
    print("나이를 정수로 입력하세요")    
else:    
    if int(age) < 20 :
           print("당신은 10대 입니다.")
    elif int(age) < 30 :
            print("당신은 20대 입니다.")
    else:
            print("당신은 30대 이상 입니다.")              
finally:
    print("무조건 실행되는 부분입니다.")