# db2.py 
import sqlite3

#연결객체를 리턴받기(파일에 영구적으로 저장)
con = sqlite3.connect("c:\\work\\sample.db")
#커서객체를 리턴받기
cur = con.cursor() 
#테이블(스키마)를 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-222');")
#입력 파라메터 처리
name = "gildong"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))
#여러건을 입력
datalist = (("tom","010-123"), ("dsp","010-456"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)
#검색
cur.execute("select * from PhoneBook;")
print(cur.fetchall())
#작업을 정상적으로 완료
con.commit()


