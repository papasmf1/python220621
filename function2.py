# function2.py 
#함수 정의(LGB 이름 해석 규칙)
x = 2 
def func(a):
    return a+x 

#호출
print(func(1))

#함수정의
def func2(a):
    x = 1 
    return a+x 

#호출
print(func2(1))

#함수의 기본값
def times(a=10, b=20):
    return a*b 

#호출
print(times())
print(times(5))
print(times(5,6))

#키워드 인자(파라매터명 명시)
def connectURI(server, port):
    strURL = "http://" + server + ":" + port 
    return strURL

#호출
print(connectURI("credu.com", "80"))
print(connectURI(port="8080", server="credu.com"))

#가변인자 함수
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출
print(union("HAM","SPAM"))
print(union("HAM","SPAM","EGG"))

#정의되지 않은 인자(필수, 옵션)
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL 

#호출
print(userURIBuilder("credu.com","80", id="kim", passwd="1234"))
print(userURIBuilder("credu.com","80", id="kim", passwd="1234",
    name="mike"))

#람다 함수(간결한 함수 정의)
g = lambda x,y:x*y 
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())

