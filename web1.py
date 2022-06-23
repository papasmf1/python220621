# web1.py 
#웹크롤링을 위한 선언
from bs4 import BeautifulSoup

#페이지 로딩
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체 
soup = BeautifulSoup(page, "html.parser")
#문서를 그대로 보기 
print(soup.prettify())

