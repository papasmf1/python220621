# function1.py 
#함수를 정의
def times(a,b):
    return a+b, a*b 

#함수를 호출
#디버깅할 때 중단(중단점)
result = times(3,4)
print(result)

#불변형식인 경우
a = 1.2 
print(id(a))
a = 2.3
print(id(a))
print("가변형식")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

#참조를 복사 전달
def change(x):
    #복사본(Deep Copy)
    x1 = x[:]
    x1[0] = "H"
    print("함수 내부:", x1)

#호출
wordlist = ["J","A","M"]
change(wordlist)
print("함수 호출후:", wordlist)

#교집합 함수(디버깅 연습)
def intersect(prelist, postlist):
    #지역변수로 교집합 문자 저장
    result = []
    #H(0) | A(1) | M(2) 
    for x in prelist:
        #x라는 글자가 postlist이 포함 그리고 x가 아직 result에 없다. 
        if x in postlist and x not in result:
            result.append(x)
    return result 

#함수 호출
print(intersect("HAM","SPAM"))


