import csv, re, os
import pymysql
 
def get_data(city: str) -> set:
    try:
        with pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="p@ssw0rd", 
            charset="utf8", 
            database="online_movie_rating", 
        ) as connection:
            with connection.cursor() as cursor:
                select_query = "select city, avg(amount) avgamt from apt where city like %s group by city order by avgamt asc"
                cursor.execute(select_query, ('%'+city+'%',))
                result = cursor.fetchone()
                return result
 
    except Error as e:
        print(e)
 
 
def init_db():
    try:
        with pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="p@ssw0rd", 
            charset="utf8", 
            database="online_movie_rating", 
        ) as connection:
            with connection.cursor() as cursor:
                delete_query = "delete from apt"
                cursor.execute(delete_query)
                
                with open('apt_data.csv', 'r') as file:
                    apt_data = csv.reader(file)
 
                    start = False
                    for apt in apt_data:
                        if len(apt) < 2 or apt[0] == '시군구':  # 헤더 부분은 처리를 생략
                            continue
                        
                        city = apt[0]
                        amount = int(apt[8].replace(',', ''))
 
                        insert_query = "insert into apt (city, amount) values (%s, %s)"
                        cursor.execute(insert_query, (city, amount, ))
 
                connection.commit()
 
    except Error as e:
        print(e)
 
def insert_data():
    city = input("지역: ")
    amount = input("거래금액: ")
 
    try:
        with pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="p@ssw0rd", 
            charset="utf8", 
            database="online_movie_rating", 
        ) as connection:
            with connection.cursor() as cursor:
                insert_query = "insert into apt (city, amount) values (%s, %s)"
                cursor.execute(insert_query, (city, amount,))
                connection.commit()
                print("정상적으로 등록되었습니다.")
 
    except Error as e:
        print(e)
 
    return None
 
def main():
    while True:
        city = input('조회할 시군구는? (Q: 종료, I: 초기화, N: 신규데이터추가, 지역명) ')
        if city.upper() == 'Q':
            break
        elif city.upper() == 'I':
            init_db()
        elif city.upper() == 'N':
            insert_data()
        else:
            result = get_data(city)
            print('"{}" 평균 거래 금액은 {:,}만원입니다.'.format(result[0], result[1]))
 
if __name__ == "__main__":
    main()        







