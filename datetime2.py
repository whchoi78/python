import datetime
import time

now = datetime.datetime.now()
print(now.strftime("%Y{}%m{}%d{} %H{}%M{}%S{}".format(*"년월일시분초")))  

#년도를 제외한 시간 되돌리기 기능
after = now + datetime.timedelta(\
    weeks=2, days=1, hours=1, minutes=1, seconds=1)
print(after.strftime("%Y{}%m{}%d{} %H{}%M{}%S{}".format(*"년월일시분초")))     


print("start")
time.sleep(3) #3초 뒤 코드 실행
print("end")