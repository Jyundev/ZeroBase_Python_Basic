# 함수를 이용한 프로그래밍
def add(n1, n2):
    return print(f'{n1} + {n2} : {n1 + n2}')


def sub(n1, n2):
    return print(f'{n1} - {n2} : {n1 - n2}')


def mul(n1, n2):
    return print(f'{n1} * {n2} : {n1 * n2}')


def div(n1, n2):
    return print(f'{n1} / {n2} : {n1 / n2}')


def mod(n1, n2):
    return print(f'{n1} % {n2} : {n1 % n2}')


def flo(n1, n2):
    return print(f'{n1} // {n2} : {n1 // n2}')


def exp(n1, n2):
    return print(f'{n1} ** {n2} : {n1 ** n2}')


print('-' * 30)

while True:
    operate = int(input('1.덧셈 \t 2.뺄셈 \t 3.곱셈 \t 4.나눗셈 \t 5.나머지 \t 6.몫 \t 7.제곱승 \t 8.종료 : '))
    if operate == 8:
        print('Bye~')
        break

    n1 = float(input('첫 번째 숫자 입력 : '))
    n2 = float(input('두 번째 숫자 입력 : '))

    if operate == 1:
        add(n1, n2)
    elif operate == 2:
        sub(n1, n2)
    elif operate == 3:
        mul(n1, n2)
    elif operate == 4:
        div(n1, n2)
    elif operate == 5:
        mod(n1, n2)
    elif operate == 6:
        flo(n1, n2)
    elif operate == 7:
        exp(n1, n2)
    else:
        print('다시 입력해주세요')
