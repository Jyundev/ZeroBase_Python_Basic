# num1 = 13
# num2 = 223.456
# sum = num1 + num2
# print("num1+num2=%.2f" % sum)
#
# partTimeMoney = int(input("알바비:"))
# cardMoney = int(input("카드값:"))
# result = partTimeMoney - cardMoney
# print('알바비 : {}  -  카드값 : {} = 잔액 : {}'.format(partTimeMoney, cardMoney, result))

# str = 'hi '
# print("{}".format(str * 8))

# num1 = 3
# num2 = 1
# print(f"{num1} 나누기 {num2} \n몫 = {num1 / num2} 나머지 = {num1 % num2}")
#
# result = divmod(num1, num2)
# print("몫 : %.0f" % result[0])
# print("나머지 : %d" % result[1])
#
#
# allStudent = int(input("전체 학생 수 : "))
# studentGroup = int(input("모둠 별 학생 수 :"))
# groupCnt = int(allStudent / studentGroup)
# overStudent = allStudent % studentGroup
#
# print(f'모둠 수 : {groupCnt}  남은 학생 수 : {overStudent}')
#
# num1 = 2
# num2 = 3
#
# result = num1 ** num2
# print(result)

# result1 = 2 ** (1 / 2)
# result2 = 2 ** (1 / 3)
# result3 = 2 ** (1 / 4)
#
# print("2의 2제곱근 : %.2f" % result1)
# print("2의 3제곱근 : %.2f" % result2)
# print("2의 4제곱근 : %.2f" % result3)

import math

#
# print("2의 2제곱근 : %.2f" % math.sqrt(2))
# print("2의 3제곱근 : %.2f" % math.sqrt(3))
# print("2의 4제곱근 : %.2f" % math.sqrt(4))
#
# print("3의 거듭 제곱 : %d" % math.pow(3, 2))
# print("3의 세제곱 : %d" % math.pow(3, 3))
# print("3의 네제곱 : %d" % math.pow(3, 4))

# firstMonthMoney = 200
# after12Month = int(firstMonthMoney * math.pow(2, 11))
# print(f"1월 용돈 : {firstMonthMoney} ... 12월 용돈 : {after12Month}")
#
#
# rainAvgAmount = 0
# totalAmount = 0
#
# totalAmount += 30
# print(f"1월 누적 강수량 : {totalAmount}")
#
# totalAmount += 50
# print(f"2월 누적 강수량 : {totalAmount}")
#
# totalAmount += 120
# print(f"3월 누적 강수량 : {totalAmount}")
#
# totalAmount += 40
# print(f"4월 누적 강수량 : {totalAmount}")
#
# totalAmount += 75
# print(f"5월 누적 강수량 : {totalAmount}")
#
# rainAvgAmount = totalAmount / 5
# print("평균 강수량 : %.2f" % rainAvgAmount)
# print(f"전체 강수량 : {totalAmount}")

# maxLength = 5200
# maxWidth = 1985
#
# myCarLength = int(input("전장 길이 : "))
# myCarWidth = int(input("전폭 길이 : "))
#
# print(f'전장 가능 여부 : {myCarLength <= maxLength}')
# print(f'전폭 가능 여부 : {myCarWidth <= maxWidth}')

# char1 = 'A'  # 65
# char2 = 'H'  # 72
#
# print('\'{}\' > \'{}\' : {}'.format(char1, char2, char1 > char2))
# print('\'{}\' >= \'{}\' : {}'.format(char1, char2, char1 >= char2))
# print('\'{}\' < \'{}\' : {}'.format(char1, char2, char1 < char2))
# print('\'{}\' <= \'{}\' : {}'.format(char1, char2, char1 <= char2))
# print('\'{}\' == \'{}\' : {}'.format(char1, char2, char1 == char2))
# print('\'{}\' != \'{}\' : {}'.format(char1, char2, char1 != char2))

# # 문자 -> 아스키 코드
# print(' \'a\' -> {} '.format(ord('a')))
# print(' \'h\' -> {} '.format(ord('h')))
#
# # 아스키 코드 -> 문자
# print(' 97 -> {} '.format(chr(97)))
# print(' 104 -> {} '.format(chr(104)))
#
# str1 = "Hello"
# str2 = "hello"
#
# print(f"{str1} == {str2} : {str1 == str2}")
# print(f"{str1} != {str2} : {str1 != str2}")
# print(f"{str1} > {str2} : {str1 > str2}")
# print(f"{str1} < {str2} : {str1 < str2}")

# print('{} and {} : {}'.format(True, True, True and False))
# print('{} and {} : {}'.format(True, True, True and True))
# print('{} or {} : {}'.format(True, True, True or True))
# print('{} or {} : {}'.format(True, True, True or False))
# print('{} not : {}'.format(True, (not True)))
# print('{} not : {}'.format(False, (not False)))


# mathScore = int(input("수학 : "))
# engScore = int(input("영어 : "))
# korScore = int(input("국어 : "))
# passScore = 60
# avg = (mathScore + engScore + korScore) / 3
# mathResult = mathScore >= 60
# engResult = engScore >= 60
# korResult = korScore >= 60
# result = ((avg > 70) and mathResult and engResult and korResult)
#
# print(f"math : {mathResult} | eng : {engResult} | kor : {korResult} | PASS : {result}")

import operator
import random

# num1 = 8
# num2 = 3
#
# print("{} + {} = {}".format(num1, num2, operator.add(num1, num2)))
# print("{} - {} = {}".format(num1, num2, operator.sub(num1, num2)))
# print("{} / {} = {}".format(num1, num2, operator.truediv(num1, num2)))
# print("{} % {} = {}".format(num1, num2, operator.mod(num1, num2)))
# print("{} // {} = {}".format(num1, num2, operator.floordiv(num1, num2)))
# print("{} ** {} = {}".format(num1, num2, operator.pow(num1, num2)))

# num1 = 8
# num2 = 3
# print("{} == {} = {}".format(num1, num2, operator.eq(num1, num2)))
# print("{} != {} = {}".format(num1, num2, operator.ne(num1, num2)))
# print("{} > {} = {}".format(num1, num2, operator.gt(num1, num2)))
# print("{} >= {} = {}".format(num1, num2, operator.ge(num1, num2)))
# print("{} < {} = {}".format(num1, num2, operator.lt(num1, num2)))
# print("{} <= {} = {}".format(num1, num2, operator.le(num1, num2)))
#
#
# print("{} and {} = {}".format(num1, num2, operator.and_(num1, num2))) #논리곱
# print("{} or {} = {}".format(num1, num2, operator.or_(num1,num2))) #논리합
# print("not {} = {}".format(num1, operator.not_(num1)))

# age = int(input("나이 : "))
# vaccine = operator.or_(operator.ge(age, 65), operator.lt(age, 20))
#
# print(f'age : {age} vaccine : {vaccine}')

# randomInt = random.randint(10, 100)
# num10 = operator.floordiv(randomInt, 10)
# num1 = operator.mod(randomInt, 10)
#
# print(f"랜덤 숫자 : {randomInt}")
# print(f"십의 자리 : {num10}\n일의 자리 : {num1}")
# print(f"십의 자리 : {num10}\n일의 자리 : {num1}")
# print(f"십의 자리가 3의 배수 인가 : {operator.mod(num10, 3) == 0} ")
# print(f"일의 자리가 3의 배수 인가 : {operator.mod(num1, 3) == 0} ")
