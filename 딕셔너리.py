#학생 정보 저정할 딕셔너리 선언
student = {"학번":201558038, "이름":"온코스", "학과":"컴공"}
print(student)

#딕셔너리에 연락처 추가
student["연락처"] = "010-4613-5221"
print(student)

#이미 존재하는 키를 사용하면 기존 값 변경
student["학과"] = "정보보안과"
print(student)

#딕셔너리 값에 접근하는 방법
print(student["학번"], student.get("학번"))
print(student["이름"], student.get("이름"))
print(student["학과"], student.get("학과"))

#딕셔너리에 없는 키 호출
print(student.get("학년"))

