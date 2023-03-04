# 미세먼지 차량 운행 제한 프로그램
import datetime

dust = int(input('미세먼지 수치 입력 : '))
carType = int(input('차량 종류 선택 - [1. 승용차  2, 영업용 차] : '))
carNum = int(input('차량 번호 입력 : '))
carLimit = ''
day = datetime.datetime.today().day

if dust <= 150 and carNum % 5 == day % 5:
    carLimit = '차량 5부제'
elif dust > 150 and carNum % 2 == day % 2:
    if carType == 1:
        carLimit = '차량 2부제'
    elif carType == 2:
        carLimit = '차량 5부제'
    else:
        carLimit = '다시 입력해주세요'
        exit(0)
else:
    carLimit = '운행 가능합니다'

print('-' * 20)
print(datetime.datetime.now())
print('-' * 20)
print(f'{carLimit} ')
print('-' * 20)
