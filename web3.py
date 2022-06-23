# web2.py 
import urllib.request
from bs4 import BeautifulSoup

#파일로 저장 
f = open("c:\\work\\webtoon.txt", "wt", encoding="utf-8")
#동적으로 주소 생성
for i in range(1,6): 
    #웹페이지의 실행결과를 문자열로 받기 
    url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + \
        str(i)
    print(url)
    data = urllib.request.urlopen(url)
    #검색을 할 객체 생성 
    soup = BeautifulSoup(data, "html.parser")
    cartoons = soup.find_all("td", class_="title")

    for item in cartoons:
        title = item.find("a").text 
        print(title.strip())
        f.write(title.strip() + "\n")
f.close()
print("웹 크롤링 종료")
