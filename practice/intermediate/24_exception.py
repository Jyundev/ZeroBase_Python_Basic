# 회원가입 프로그램

class DataEmptyException(Exception):
    def __init__(self, val):
        super().__init__(f'{val} is empty')


class Member:
    def __init__(self, name, mail, pw, address, phone):
        self.name = name
        self.mail = mail
        self.pw = pw
        self.address = address
        self.phone = phone
        print('Membership completed!!')

    def printMemberInfo(self):
        print(f'name : {self.name}')
        print(f'mail : {self.mail}')
        print(f'pw : {self.pw}')
        print(f'address : {self.address}')
        print(f'phone : {self.phone}')


def registerMember():
    name = input('이름 입력 : ')
    mail = input('메일 입력 : ')
    pw = input('비밀번호 입력 : ')
    address = input('주소 입력 : ')
    phone = input('연락처 입력 : ')

    if name == '':
        raise DataEmptyException('name')
    if mail == '':
        raise DataEmptyException('mail')
    if pw == '':
        raise DataEmptyException('pw')
    if address == '':
        raise DataEmptyException('address')
    if phone == '':
        raise DataEmptyException('phone')

    mem = Member(name, mail, pw, address, phone)
    mem.printMemberInfo()


try:
    registerMember()
except DataEmptyException as e:
    print(e)
