# BankAccount.py
#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #클래스 내부에 숨겨달라(이름 변경)
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
account1.deposit(5000)
#이름에 접근
#print(account1.__balance)
#외부에서는 _클래스명__변수명(백도어-테스트)
print(account1._BankAccount__balance)
print(account1)
