import pymysql


#mysql 서버에 연결
conn = pymysql.connect(\
    host='localhost',\
    user='root',\
    password='1234',\
    db='employees',\
) 

cursor = conn.cursor() #커서 생성

sql ="SELECT * FROM employees"

cursor.execute(sql) #쿼리문 실행
# result = cursor.fetchone() #결과 가져오기(한번의 호출로 하나의 행을 가져옴)
result = cursor.fetchall() #결과 가져오기(한번의 호출로 모든 행을 가져옴)
# result = cursor.fetchmany(5) #결과 가져오기(한번의 호출로 5개의 행을 가져옴)
print(result) #결과 출력
conn.close() #연결 해제