# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#파일 생성(기존 파일에 첨부)
f = open("c:\\work\\humor.txt", "a+", encoding="utf-8")
for n in range(1,11):
        #오늘의 유머 베스트오브게시판 
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우는 디코딩
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})
        # <td class="subject">
        #     <a href="/board/view.php?table=bestofbest">
        #     세상은 메타버스라는 스님</a>
        # </td>
        for item in list:
                try:
                        title = item.find("a").text
                        #print(title.strip())
                        if (re.search('누리호', title)):
                            print(title.strip())
                            f.write(title.strip() + "\n")
                except:
                        pass
        

f.close() 
print("웹 크롤링 종료")
