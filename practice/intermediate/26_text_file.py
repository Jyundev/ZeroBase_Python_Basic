# 텍스트 파일 읽기/쓰기
import datetime
import time

path = "C:/Users/YUN/Python/"


class User:
    def __init__(self, id, pw):
        self.id = id
        self.pw = pw
        self.diary = ''


class ManagerUser:
    def __init__(self):
        self.users = {}

    def join(self, user):
        if user.id in self.users:
            print(f'{user.id}는 이미 존재하는 ID 입니다.')
        else:
            self.users[user.id] = user

        for id in self.users.keys():
            allUser = self.users[id]
            print(f'ID : {allUser.id}\t | \tPW : {allUser.pw}')

    def writeDiary(self, user):
        if user.id in self.users:
            checkUser = self.users[user.id]
            if checkUser.pw == user.pw:
                print('\t Login Success \t')
                # time = datetime.datetime.now()
                lt = time.localtime()
                timeStr = time.strftime('%Y-%m-%d %I:%M:%S %p', lt)
                # 파일 쓰기
                txt = input('오늘 하루 인상 깊은 일을 기록하세요 : ')
                with open(path + f'_{user.id}.txt', 'a') as file:
                    file.write(f'[{timeStr}] {txt}\n')
                    user.diary = f'{path}_{user.id}.txt'

                self.users[user.id] = user
            else:
                print(f'올바르지 않은 패스워드입니다.')
        else:
            print(f'{user.id} 존재하지 않는 ID 입니다')

    def viewDiary(self, user):
        if user.id in self.users:
            checkUser = self.users[user.id]
            if checkUser.pw == user.pw:
                print('\t Login Success \t')

                # 파일 읽기
                with open(checkUser.diary, 'r') as file:
                    line = file.readline()
                    while line != '':
                        print(line)
                        line = file.readline()
            else:
                print(f'올바르지 않은 패스워드입니다.')

        else:
            print(f'{user.id} 존재하지 않는 ID 입니다')


manage = ManagerUser()

while True:

    try:
        n = int(input('1. 회원가입  2. 한줄일기쓰기 3. 한줄일기보기 4. 종료 : '))
        if n not in [1, 2, 3, 4]:
            print('다시 입력하세요')
            continue
        if n == 4:
            print('\t 종료합니다 \t')
            break

    except Exception as e:
        print(e)
        continue

    id = input('input ID : ')
    pw = input('input PW : ')
    user = User(id, pw)

    if n == 1:
        manage.join(user)
    if n == 2:
        manage.writeDiary(user)
    if n == 3:
        manage.viewDiary(user)
