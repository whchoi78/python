import datetime

now = datetime.datetime.now()
print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")

print(now.strftime("%Y.%m.%d %H:%M:%S"))
print("{}년 {}월 {}일 {}시 {}분 {}초".format(\
    now.year, \
        now.month, \
            now.day, \
                now.hour, \
                    now.minute, \
                        now. second))
# *를 붙혀 주면 요소 하나하나가 매개변수로 지정 된다
print(now.strftime("%Y{}%m{}%d{} %H{}%M{}%S{}".format(*"년월일시분초")))                        