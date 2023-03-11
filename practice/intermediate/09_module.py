# 로또 모듈 프로그램
import random
import CustomModule.lotto as lt

numbers = []

for i in range(6):
    n = int(input('번호(1~45) 입력 : '))
    numbers.append(n)

lt.getLottoResult(numbers)
