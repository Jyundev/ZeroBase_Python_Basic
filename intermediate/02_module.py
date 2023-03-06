import random

# rNum = random.randint(1, 10)
# print(f'모듈 rand 이용 : {rNum}')

# rNums = random.sample(range(101), 10)
# print(rNums)

# import UserModule.calculator as cal
#
# cal.add(10, 20)
# cal.sub(10, 20)
# cal.mul(10, 20)
# cal.div(10, 20)

# import UserModule.lotto_make as lotto
#
# lotto.numbers()
#
# import UserModule.reverse as reverse
#
# print(reverse.getReverseStr("Hello"))
#
# from UserModule.calculator import add
# from UserModule.calculator import sub
# from UserModule.calculator import mul, div
# from UserModule.calculator import *
#
# add(10, 20)
# sub(10, 20)
# mul(10, 20)
# div(10, 20)

# import UserModule.score as score
#
# korScore = int(input('국어 점수 입력 : '))
# engScore = int(input('영어 점수 입력 : '))
# mathScore = int(input('수학 점수 입력 : '))
#
# score.addKor(korScore)
# score.addEng(engScore)
# score.addMath(mathScore)
#
# print(f'총점 : {score.getTotalScore()}')
# print(f'평균 : {score.getAvgScore()}')

# from UserModule.calculator import *
#
# add(10, 20)
# print(f'{__name__}')
#
# import UserModule.unitConversion as converse
#
# if __name__ == '__main__':
#     n = int(input('숫자 입력(cm) : '))
#     print(f'10cm : {converse.cmToMM(n)}')
#     print(f'10cm : {converse.cmToInch(n)}')
#     print(f'10cm : {converse.cmToM(n)}')
#     print(f'10cm : {converse.cmToFt(n)}')

# from CalculatorForFloat import addCal
# from CalculatorForFloat import subCal
# from CalculatorForFloat import mulCal
# from CalculatorForFloat import divCal
#
# print(addCal.add(10, 20))
# print(subCal.sub(10, 20))
# print(mulCal.mul(10, 20))
# print(divCal.div(10, 20))
#
# from CalculatorForInt import addCal
# from CalculatorForInt import subCal
# from CalculatorForInt import mulCal
# from CalculatorForInt import divCal
#
# print(addCal.add(10, 20))
# print(subCal.sub(10, 20))
# print(mulCal.mul(10, 20))
# print(divCal.div(10, 20))

# import sys
#
# for path in sys.path:
#     print(path)
#
# #C:\Users\YUN\Python\project\venv\lib\site-packages
# #venv : 가상환경
#

# 약수와 소수를 리스트로 변환

# import divisor_pac.divisor_mod as div
#
# print(div.divisor(98))
# print(div.prime(50))
#

# 수학 관련 함수

# 합
listvar = [2, 5, 6, 7, 8, 12]
print(sum(listvar))

# 최댓값
print(max(listvar))

# 최솟값
print(min(listvar))

# 거듭제곱
print(pow(13, 3))

# 반올림
print(round(3.141592, 1))
print(round(3.141592, 2))
print(round(3.141592, 3))

# math
import math

# 절댓값
print(math.fabs(-10))

# 올림
print(math.ceil(5.31))
print(math.ceil(-5.31))

# 내림
print(math.floor(5.31))
print(math.floor(-5.31))

# 버림
print(math.trunc(5.31))
print(math.trunc(-5.31))

# 최대공약수
print(math.gcd(14, 21))

# 팩토리얼
print(math.factorial(10))

# 제곱근
print(math.sqrt(14))

# time

import time

lt = time.localtime()
print(lt)

print(lt.tm_year)
print(lt.tm_mon)
print(lt.tm_mday)
print(lt.tm_hour)
print(lt.tm_min)
print(lt.tm_sec)
