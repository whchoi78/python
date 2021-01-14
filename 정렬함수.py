st = "python"
#숫자만큼 전체 자릿수를 잡은 후 가운데 정렬
print(st.center(10))
#남은 공간은 "-"로 채움
print(st.center(10, '-'))

#왼쪽 정렬
print(st.ljust(10), st.ljust(10))

#오른쪽 정렬
print(st.rjust(10), st.rjust(10))

#오른쪽 정렬 후 남은 공간은 0으로 채움
print(st.zfill(10))
