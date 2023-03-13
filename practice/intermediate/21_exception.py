# 예외처리를 이용한 산술연산 프로그램


def add(n1, n2):
    try:
        n1 = float(n1)
        n2 = float(n2)
        print(f'{n1} + {n2} : {n1 + n2}')
    except:
        print(f'숫자만 입력하세요')


def sub(n1, n2):
    try:
        n1 = float(n1)
        n2 = float(n2)
        print(f'{n1} - {n2} : {n1 - n2}')
    except:
        print(f'숫자만 입력하세요')


def mul(n1, n2):
    try:
        n1 = float(n1)
        n2 = float(n2)
        print(f'{n1} * {n2} : {n1 * n2}')
    except:
        print(f'숫자만 입력하세요')


def div(n1, n2):
    try:
        n1 = float(n1)
        n2 = float(n2)
        # if n2 == 0:
        #     print(f'0으로 나눌 수 없습니다')
        #     return
        # else:
        #     print(f'{n1} / {n2} : {n1 / n2}')
        print(f'{n1} / {n2} : {n1 / n2}')

    except ZeroDivisionError:
        print(f'0으로 나눌 수 없습니다.')
    except:
        print(f'숫자만 입력하세요')


def mod(n1, n2):
    try:
        n1 = float(n1)
        n2 = float(n2)
        if n2 == 0:
            print(f'0으로 나눌 수 없습니다')
            return
        else:
            print(f'{n1} % {n2} : {n1 % n2}')

    except:
        print(f'숫자만 입력하세요')


def flo(n1, n2):
    try:
        n1 = float(n1)
        n2 = float(n2)
        if n2 == 0:
            print(f'0으로 나눌 수 없습니다')
            return
        else:
            print(f'{n1} // {n2} : {n1 // n2}')

    except:
        print(f'숫자만 입력하세요')


def exp(n1, n2):
    try:
        n1 = float(n1)
        n2 = float(n2)
        print(f'{n1} ** {n2} : {n1 ** n2}')
    except:
        print(f'숫자만 입력하세요')


print('-' * 30)

while True:

    try:
        operate = int(input('1.덧셈 \t 2.뺄셈 \t 3.곱셈 \t 4.나눗셈 \t 5.나머지 \t 6.몫 \t 7.제곱승 \t 8.종료 : '))
    except:
        print('다시 입력하세요.')
        continue

    if operate == 8:
        print('Bye~')
        break

    n1 = input('첫 번째 숫자 입력 : ')
    n2 = input('두 번째 숫자 입력 : ')

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
