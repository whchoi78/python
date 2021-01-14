st = "python is very fun"

#공백을 기준으로 분리해 리스트로 반환
print(st.split())

st = "python.is.very.fun"
#"."을 기준으로 분리해 리스트로 반환
print(st.split("."))

#"\n을 기준으로 분리해 리스트로 반환"
st = "python\nis\nvery\nfun"
print(st.splitlines())

st ="%"
#"python"사이에 '%'를 합쳐 줌
print(st.join("python"))
