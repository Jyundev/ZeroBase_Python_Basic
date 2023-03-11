# 순열 계산 프로그램

import CustomModule.calculation as cal

if __name__ == '__main__':
    n = int(input('numN 입력 : '))
    r = int(input('numR 입력 : '))

    cal.getPermutation(n, r, False)
