while True:
   sel = int(input("1.덧셈 2.뺄셈 3.곱셈 4.나눗셈\n선택 : "))

   if sel in [1,2,3,4]:
      n1 = int(input("첫 번째 수 입력 :"))
      n2 = int(input("두 번째 수 입력 :"))

      if sel==1:
         print("{} + {} = {} 입니다.".format(n1, n2, n1+n2))

      elif sel==2:
         print("{} - {} = {} 입니다.".format(n1, n2, n1-n2))

      elif sel==3:
         print("{} * {} = {} 입니다.".format(n1, n2, n1*n2))

      elif sel==4:
         print("{} / {} = {} 입니다.".format(n1, n2, n1/n2))
   else:
      print("잘못 입력했습니다.")            