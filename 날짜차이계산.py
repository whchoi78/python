'''
def days_difference(day1: int, day2: int):
    return day2 - day1    

def week_difference(now: int, after: int):
    return (now + after) % 7    

def get_birthday_weekday(current_weekday: int, current_day: int, birthday_day: int):
    days_diff = days_difference(current_day, birthday_day)
    return week_difference(current_day, days_diff)    

print(get_birthday_weekday(5, 3, 4))

def eval(a, b, c):
    return (a+b+c) / 3

print(eval(3,4,5))

def repeat(s: str, n: int):
    return s * n
print(repeat('yes',4))    

life = [
        ['canada', 76.5],
        ['usa', 72.0],
        ['mexico', 80]
        ]
print(life[1][0])        

n = int(input("n 입력: "))
 
print(" ", end=" ")
for x in range(1, n+1):
    print(x, end=" ")
print()
 
for y in range(1, n+1):
    print(y, end=" ")
    for x in range(1, n+1):
        print (x * y, end=" ")
    print()
'''

import urllib.request
url = 'http://people.cs.pitt.edu/~wiebe/courses/CS0007/Lectures/hopedale.dat'
hap = 0

with urllib.request.urlopen(url) as webpage:
    for a in range(0, 3):
        webpage.readline()
    for line in webpage:
        line.strip()
        line = line.decode('UTF-8')
        hap += int(line)
        
print(hap)

