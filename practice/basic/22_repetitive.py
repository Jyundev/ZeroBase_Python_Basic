'''
윤년 계산기
연도가 4로 나누어 떨어지고 100으로 나누어 떨어지지 않으면 윤년이다.
또는 연도가 400으로 나누어 떨어지면 윤년이다.
'''

year = int(input('연도 입력 : '))

if year % 4 == 0 and year % 100 != 0:
    print(f'{year}년 : 윤년')
elif year % 400 == 0:
    print(f'{year}년 : 윤년')
else:
    print(f'{year}년 : 평년')
