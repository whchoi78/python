st = "PYTHON 123 is very fun"
#문자열 숫자로 되어 있는지 여부 반환
print(st.isdigit(), st[7:10].isdigit())

#영문자로 이뤄져 있는지 여부 반환
print(st.isalpha(), st[0:6].isalpha())

#영문자와 숫자로 이뤄져 있는지 여부 확인
print(st.isalnum())

#소문자로 이뤄져 있는지 여부 반환
print(st.islower(), st[11:13].islower())

#대문자로 이뤄져 있는지 여부 반환
print(st.isupper(), st[0:6].isupper())

#공백 문자로 이뤄져 있는지 여부 반환
print(st.isspace(), st[6:7].isspace())
