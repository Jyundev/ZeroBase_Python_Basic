# 시, 분, 초를 입력하면 초로 환산하는 프로그램
# import operator
#
# hour = int(input('시간 입력 : '))
# min = int(input('분 입력 : '))
# sec = int(input('초 입력 : '))
#
# totalSec = hour * operator.pow(60, 2) + min * 60 + sec
# print('{} 초'.format(format(totalSec, ',')))

# 금액, 이율, 거치 기간을 입력하면 복리를 계산하는 프로그램
money = int(input('금액 입력 : '))
percent = float(input('이율 입력 : '))
date = int(input('기간 입력 : '))
print()
print('-' * 30)
print()

targetMoney = money
for i in range(date):
    targetMoney += targetMoney * percent * 0.01

print(f'이율 : {percent}%')
print('원금 : {}'.format(format(money, ',')))
print('5년 후 금액 :', format(int(targetMoney), ','))
