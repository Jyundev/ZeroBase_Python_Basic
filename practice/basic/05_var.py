# 키오스크에서 사용하는 언어 선택 프로그램을 만들어보자
import datetime

# selectNum = int(input('언어 선택 (Choose Your Language) | 1. 한국어  2. English  : '))
#
# if selectNum == 1:
#     menu = '1.샌드위치 \t 2.햄버거 \t 3.쥬스 \t 4.커피 \t 5.아이스크림'
# elif selectNum == 2:
#     menu = '1.Sandwich \t 2.Hamburger \t 3.Juice \t 4.Coffee \t 5.Ice cream'
#
# print(menu)
#
# #나의 나이가 100살 되는 해의 연도를 구하는 프로그램을 만들어보자
age = int(input('나이 입력 : '))
year = datetime.date.today().year

if age < 100:
    print(f"{year + (100 - age)}년 ({100 - age}년 후)에 100살!!")
else:
    print("100세 미만만 입력 가능 ")
