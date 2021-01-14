import random

while True :
    com = random.choice(["가위","바위","보"])
    user = input("입력하세요 : ")
    print("컴퓨터 : {}".format(com))

    if user == "가위" or user == "바위" or user == "보" :
        if com == user:
            print("비겻습니다. 다시 하세요")
            print(" ")
            continue
        elif(user == "가위" and com=="보") or \
            (user == "바위" and com=="가위") or \
                (user == "보" and com=="바위"):
            print("이겼습니다.")
            break
        elif(user == "가위" and com=="바위") or \
            (user == "바위" and com=="보") or \
                (user == "보" and com=="가위"):
            print("졌습니다. 다시 하세요")
            print(" ")
            continue
    else : 
        print("잘못 냈습니다.")   