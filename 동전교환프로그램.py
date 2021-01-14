print("=====동전 교환 프로그램======")
money = int(input("금액을 입력 하세요 : "))
print("{}원".format(money))
c500 = money // 500
money = money % 500

c100 = money // 100
money = money % 100

c50 = money // 50
money = money % 50

c10 = money // 10
money = money % 10

print("500원 짜리 {}개".format(c500))
print("100원 짜리 {}개".format(c100))
print("50원 짜리 {}개".format(c50))
print("10원 짜리 {}개".format(c10))
print("잔돈 : {}원".format(money))