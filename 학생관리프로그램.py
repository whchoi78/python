studant = {}

while True:
    print("1.학생 등록", end=" ")
    print("2.학생 검색", end=" ")
    print("3.학생 수정", end=" ")
    print("4.학생 삭제", end=" ")
    print("5.전체 출력", end=" ")
    print("6.종료")
    num = int(input("옵션을 선택 하세요 : "))

    if num == 1 :
        studant.setdefault(int(input("번호를 입력하세요 : ")), \
            input("이름을 입력하세요 : "))
        print("등록 되었습니다.")
        print(studant.items())

    elif num == 2 :
        print(studant[int(input("찾고자 하는 학생의 번호를 입력하세요 : "))])

    elif num == 3 :
        num2 = int(input("수정하고자 하는 학생의 번호를 입력하세요 : "))
        studant[num2] = input("수정 하세요 : ")
        print("수정 되었습니다")
        print(studant[num2])

    elif num == 4 :
        num3 = int(input("삭제하고자 하는 학생의 번호를 입력하세요 : "))
        studant.pop(num3)
        print("삭제 되었습니다")
        print(studant.items())

    elif num == 5 :
        print(studant.items())

    elif num == 6 :
        print("종료 합니다. 수고하세요")
        break

    else :
        print("잘못입력했습니다 다시 입력하세요")