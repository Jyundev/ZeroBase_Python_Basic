# 은행 계좌 프로그램
import random


class BankException(Exception):
    def __init__(self, balance, withdraw):
        super().__init__(f'잔고부족 ! 잔액 : {balance} 출금액 : {withdraw}')


class Account:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank
        self.totalMoney = 0

        while True:
            self.no = random.randint(1000, 9999)
            if bank.isAccount(self.no):
                continue
            else:
                break

        self.printAccount()

    def printAccount(self):
        print('-' * 30)
        print(f'account_name : {self.name}')
        print(f'account_no : {self.no}')
        print(f'totalMoney : {self.totalMoney}원')
        print('-' * 30)


class Bank:
    def __init__(self):
        self.accounts = {}

    def addAccount(self, account):
        self.accounts[account.no] = account

    def isAccount(self, no):
        if no in self.accounts:
            return True
        else:
            return False

    def deposit(self, no, money):
        if no in self.accounts:
            account = self.accounts[no]
            account.totalMoney += money
        else:
            print('존재하지 않는 계좌입니다')

    def withdraw(self, no, money):
        if no in self.accounts:
            account = self.accounts[no]
            if account.totalMoney - money > 0:
                account.totalMoney -= money
            else:
                raise BankException(account.totalMoney, money)
        else:
            print('존재하지 않는 계좌입니다')


bank = Bank()
name = input('통장 계설을 위한 예금주 입력 : ')
account = Account(name, bank)
bank.addAccount(account)

while True:
    num = int(input('1. 입금, 2. 출금, 3. 종료 : '))
    if num == 1:
        money = int(input('입금액 입력 : '))
        bank.deposit(account.no, money)
        account.printAccount()
    if num == 2:
        try:
            money = int(input('출금액 입력 : '))
            bank.withdraw(account.no, money)
            account.printAccount()
        except BankException as e:
            print(e)
        finally:
            account.printAccount()
    if num == 3:
        print('종료')
        break
