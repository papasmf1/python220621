# web1.py 
#웹크롤링을 위한 선언
from bs4 import BeautifulSoup

#페이지 로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체 
soup = BeautifulSoup(page, "html.parser")
#문서를 그대로 보기 
#print(soup.prettify())

#<p>태그 전체를 검색
#print(soup.find_all("p"))

#첫번째<p>검색
#print(soup.find("p"))

#조건이 있는 경우:<p class=outer-text>
#print(soup.find_all("p", class_="outer-text"))

#id속성으로 검색
#print(soup.find_all(id="first"))

#문자열만 리턴
for item in soup.find_all("p"):
    title = item.text 
    title = title.replace("\n", "")
    print(title.strip())




