# 1부터 100까지 정수 중 십의 자리와 일의 자리에 대해 홀/짝 구분 프로그램
import operator

for i in range(1, 101):
    num10 = operator.floordiv(i, 10)  # i // 10 과 동일, i / 10 은 실수 출력
    num1 = operator.mod(i, 10)

    if i >= 10:
        if num10 % 2 == 0:
            print(f'[{i}] 십의 자리 : 짝수 ', end='')
            if num1 % 2 == 0:
                print('일의 자리 : 짝수')
            else:
                print('일의 자리 : 홀수')
        else:
            print(f'[{i}] 십의 자리 : 홀수 ', end='')
            if num1 % 2 == 0:
                print('일의 자리 : 짝수')
            else:
                print('일의 자리 : 홀수')

    else:
        if num1 % 2 == 0:
            print(f'[{i}]  일의 자리 : 짝수')
        else:
            print(f'[{i}]  일의 자리 : 홀수')
