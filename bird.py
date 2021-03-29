#새의 종류를 담을 리스트 변수 선언
#birds = []
#새의 종류를 담을 세트 변수 선언
#새 종류 별 관찰 횟수를 담을 리스트의 변수를 정의
#birds = set()
birds = {}

with open('bird_data.txt', 'r') as file:
    for line in file:
        bird = line.strip()
#        birds.add(bird)
#       리스트에 등록되어 있는지 여부를 확인        
        
        if bird in birds:
            birds[bird] = birds[bird] + 1
        else:
            birds[bird] = 1               

print(birds)            

