# DemoRandom.py 
import random

print(random.random())
print(random.random())
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))

print("---로또번호---")
lotto = list(range(1,46))
print(lotto)
random.shuffle(lotto)
print(lotto)
for item in range(5):
    print(lotto.pop())

#파일과 폴더 다루기 
from os.path import *
print(abspath("python.exe"))
print(basename("c:\\python39\\python.exe"))
print(getsize("c:\\python39\\python.exe"))
print(exists("c:\\python39\\python.exe"))

#운영체제 정보 보기
from os import * 
print(getcwd())
print(name)
#system("notepad.exe")

#파일, 폴더리스트 
import glob 
result = glob.glob("c:\\work\\*.py")
print(result)

