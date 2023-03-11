# 연산 계산기 + 넓이 구하기 프로그램

from arithmetic.basic_operator import *
from arithmetic.developer_operator import *
from shape.triangle_square_area import *
from shape.circle_area import *

n1 = float(input('숫자1 입력 : '))
n2 = float(input('숫자1 입력 : '))
# add
print(f'{n1} + {n2} : {add(n1, n2)}')
print(f'{n1} - {n2} : {sub(n1, n2)}')
print(f'{n1} * {n2} : {mul(n1, n2)}')
print(f'{n1} / {n2} : {div(n1, n2)}')
print(f'{n1} % {n2} : {mod(n1, n2)}')
print(f'{n1} // {n2} : {flo(n1, n2)}')
print(f'{n1} ** {n2} : {exp(n1, n2)}')

w = float(input('가로 입력 : '))
h = float(input('세로 입력 : '))
print(f'삼각형 넓이 : {getTriangleArea(w, h)}')
print(f'사각형 넓이 : {getSquareArea(w, h)}')

r = float(input('반지름 입력 : '))
print(f'원의 넓이 : {getCircleArea(r)}')
