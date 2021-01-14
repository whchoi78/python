hour = int(input("시를 입력 하세요 : "))
minute = int(input("분을 입력 하세요 : "))

minute = minute + hour * 60
if minute < 30 :
    minute += 30
    print("23시 {}분".format(minute))

else:
    pass   
    minute -= 30
    hour = minute // 60
    minute %= 60
    print("{}시 {}분".format(hour, minute))

