# 수입과 지출을 기록하는 가계부
import time

path = "C:/Users/YUN/Python/"


class AccountBook:
    def __init__(self):
        self.deposit = 0
        self.type = ''
        self.balance = 0

    def doDeposit(self):
        money = int(input('입금액 입력 : '))
        self.type = input('입금 내역 입력 : ')
        print('입금완료!!!!')
        print(f'기존 잔액 : {self.balance}')
        self.balance += money
        print(f'입금 후 잔액 : {self.balance}')

        self.writeRecipt(0, money)

    def doWithdraw(self):
        money = int(input('출금액 입력 : '))
        self.type = input('출금 내역 입력 : ')
        if money < self.balance:
            print('출금완료!!!!')
            print(f'기존 잔액 : {self.balance}')
            self.balance -= money
            print(f'입금 후 잔액 : {self.balance}')

            self.writeRecipt(1, money)
        else:
            print('잔액이 부족합니다.')

    def writeRecipt(self, n, money):  # n==0 입금 n==1 출금
        lt = time.localtime()
        strf_time = time.strftime('%Y-%m-%d %I:%M:%S')
        if n == 0:
            recipt = f'{"-" * 30}\n{strf_time}\n[입금] {self.type} : {money}원\n[잔액] ' \
                     f'{self.balance}원\n{"-" * 30}\n'
            with open(path + 'accountBook.txt', 'a') as f:
                f.write(recipt)

        if n == 1:
            recipt = f'{"-" * 30}\n{strf_time}\n[출금] {self.type} : {money}원\n[잔액] ' \
                     f'{self.balance}원\n{"-" * 30}\n'
            with open(path + 'accountBook.txt', 'a') as f:
                f.write(recipt)


account = AccountBook()
while True:
    n = int(input('1. 입금 2. 출금 3. 종료 : '))
    if n == 1:
        account.doDeposit()
    elif n == 2:
        account.doWithdraw()
    elif n == 3:
        break
    else:
        print('다시 입력')
