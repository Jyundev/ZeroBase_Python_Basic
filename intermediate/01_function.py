# def addFun(x, y):
#     return x + y
#
#
# print(addFun(3, 4))
import random

# def addCal():
#     n1 = int(input('n1 : '))
#     n2 = int(input('n2 : '))
#     print(f'n1 + n2 : {n1 + n2}')
#
#
# n1 = int(input('n1 : '))
# n2 = int(input('n2 : '))
# print(f'n1 + n2 : {n1 + n2}')

# 정수 두개 입력하면 곱셈 나눗셈 출력
# def calFuc():
#     n1 = int(input('n1 : '))
#     n2 = int(input('n2 : '))
#     print(f'{n1} * {n2} : {n1 * n2}')
#     print(f'{n1} / {n2} : {round(n1 / n2, 2)}')  # 반올림 함수 : 두번째 자리에서 반올림
#
#
# calFuc()
# calFuc()
# calFuc()
#
# def fun1():
#     print('fun1 호출')
#     fun2()
#     print('fun2 호출 후 호출')
#
#
# def fun2():
#     print('fun2 호출')
#     fun3()
#
#
# def fun3():
#     print('fun3 호출')
#
#
# fun1()
# def fun3():
#     pass

# def gugudan2():
#     gugudan3()
#     for i in range(1, 10):
#         print(f'2 * {i} ={2 * i}')
#
#
# def gugudan3():
#     gugudan4()
#     for i in range(1, 10):
#         print(f'3 * {i} ={3 * i}')
#
#
# def gugudan4():
#     gugudan5()
#     for i in range(1, 10):
#         print(f'4 * {i} ={4 * i}')
#
#
# def gugudan5():
#     for i in range(1, 10):
#         print(f'5 * {i} ={5 * i}')
#
#
# gugudan2()

# def great(hello):
#     print(f'{hello}')
#
#
# great('안녕')
# def cal(n1, n2):
#     print(f'{n1} + {n2} = {n1 + n2}')
#     print(f'{n1} - {n2} = {n1 - n2}')
#     print(f'{n1} * {n2} = {n1 * n2}')
#     print(f'{n1} // {n2} = {n1 // n2}')
#
#
# cal(20, 5)

# def printNum(*numbers):
#     for number in numbers:
#         print(number, end='')
#
#
# printNum()
# printNum(10)
# printNum(20, 20)
# printNum(10, 20, 30)

# def printScore(kor, eng, math):
#     print(f'총점 : {kor + eng + math}')
#     print(f'평균 : {(kor + eng + math) // 3}')
#
#
# kor = int(input('국어 점수 : '))
# eng = int(input('영어 점수 : '))
# math = int(input('수학 점수 : '))
#
# printScore(kor, eng, math)

# def cal(n1, n2):
#     return n1 + n2
#
#
# returnValue = cal(20, 10)
# print(f'returnValue : {returnValue}')

# def divideNumber(n):
#     if n % 2 == 0:
#         return '짝수'
#     else:
#         return '홀수'
#
#
#
# print(divideNumber(5))
#

# def getOddRandomNember():
#     while True:
#         num = random.randint(1, 100)
#         if num % 2 == 0:
#             pass
#         else:
#             break
#
#     return num
#
#
# print(f'returnRandNum : {getOddRandomNember()}')

# num_out = 10
#
#
# def printNumber():
#     num_out = 20 #함수의 지역변수
#     print(f'num_out : {num_out} [함수 안]')
#
#
# printNumber()
# print(f'num_out : {num_out} [함수 밖]')

# def printNumber():
#     num_in = 20 #함수의 지역변수
#     print(f'num_out : {num_in} [함수 안]')
#
# print(f'num_out : {num_in} [함수 밖]')

num_out = 10

# def printNumber():
#     global num_out #global 키워드
#     num_out = 20
#     print(f'num_out : {num_out} [함수 안]')
#
#
# printNumber()
# print(f'num_out : {num_out} [함수 밖]')

# totalVisit = 0
# def count():
#     global totalVisit
#     totalVisit += 1
#     print('누적 방문객 : ', totalVisit)
#
#
# count()
# count()
# count()
# count()
# count()
# count()
# count()

# def out_function():
#     print('out_function called')
#
#     def in_function():
#         print('in_function called')
#
#     in_function()
#
#
# out_function()
# in_function() # Error

# def calculator(n1, n2, cal):
#     def add():  # 0
#         print(f'{n1} + {n2} = {n1 + n2}')
#
#     def sub():  # 1
#         print(f'{n1} - {n2} = {n1 - n2}')
#
#     def mul():  # 2
#         print(f'{n1} * {n2} = {n1 * n2}')
#
#     def div():  # 3
#         print(f'{n1} / {n2} = {round(n1 / n2, 2)}')
#
#     if cal == 0:
#         add()
#     elif cal == 1:
#         sub()
#     elif cal == 2:
#         mul()
#     elif cal == 3:
#         div()
#     else:
#         print('다시 입력')
#
#
# calculator(2, 3, 0)
# calculator(2, 3, 1)
# calculator(2, 3, 2)
# calculator(2, 3, 3)

# def calculator(n1, n2):
#     return n1 + n2
#
#
# value = calculator(2, 3)
# print(value)
#
# calculator_lambda = lambda n1, n2: n1 + n2
# value = calculator_lambda(3, 4)
# print(value)

getTriangleArea = lambda n1, n2: n1 * n2 / 2
getSquareArea = lambda n1, n2: n1 * n2
gerCircleArea = lambda r: r * r * 3.14

width = int(input('가로 길이 입력 : '))
height = int(input('세로 길이 입력 : '))
radius = int(input('반지름 길이 입력 : '))
print(f'삼각형의 넓이 : {getTriangleArea(height, width)}')
print(f'사각형의 넓이 : {getSquareArea(height, width)}')
print(f'원의 넓이 : {gerCircleArea(radius)}')
