# 조합 계산 모듈

import CustomModule.calculation as cal

if __name__ == '__main__':
    n = int(input('numN 입력 : '))
    r = int(input('numR 입력 : '))

    cal.getCombination(n, r, False)
