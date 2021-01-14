import os

#현재 운영체제의 이름을 확인해줌
print(os.name)

#현재 폴더
print(os.getcwd())

#현재 폴더에 있는 파일 목록 확인
print(os.listdir())

#폴더 생성, 삭제
#os.mkdir("test")
#os.rmdir("test")

#파일 생성
'''
with open("A.txt", "w") as file:
    file.write("hello")
os.rename("A.txt", "B.txt")
os.remove("B.txt")
'''

#시스템 명령어 실행
os.system("dir")