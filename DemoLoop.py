# DemoLoop.py 
#반복구문 
value = 5 
while value > 0:
    print(value)
    value -= 1 

print("---반복 종료---")

#순회가능한 형식(시퀀스형식)
for item in [1,2,3]:
    print(item)

#구구단 출력
for x in [2,3,4,5,6]:
    print("---{0}단 출력---".format(x))
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x,y,x*y))

print("---break---")
lst = list(range(1,11))
print(lst)
for i in lst:
    if i > 5:
        break 
    print("Item:{0}".format(i))

print("---continue---")
for i in lst:
    # %는 나머지값 
    if i % 2 == 0:
        continue 
    print("Item:{0}".format(i))

years = list(range(2000, 2023))
print(years)
days = list(range(1,32))
print(days)

#리스트 컴프리헨션(리스트 임베딩)
lst = list(range(1,11))
print([i**2 for i in lst if i > 5])

#Tuple에 담은 데이터
tp = ("apple", "orange", "kiwi")
print([len(i) for i in tp])

#필터링 하는 함수
lst = [10, 25, 30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

print("---필터링---")
def getBiggerThan20(i):
    return i > 20

iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

print("---람다함수---")
iterL = filter(lambda i:i>20, lst)
for item in iterL:
    print(item)

