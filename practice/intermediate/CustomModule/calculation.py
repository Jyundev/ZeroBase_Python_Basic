# 순열 계산 프로그램
# 조합 계산 프로그램

from itertools import permutations

from itertools import combinations


def getPermutation(n, r, log=True):
    result = 1
    logs = []
    for i in range(n, n - r, -1):
        print(f'n : {i}')
        result *= i

    print(f'{n}P{r} : {result}')

    if log:
        for i in range(n):
            logs.append(i + 1)
        getPermutaionLog(logs, r)

    return


def getPermutaionLog(logs, r):
    logList = list(permutations(logs, r))
    print(f'{len(logs)}P{r} 개수: {len(logList)}')

    for n in logList:
        print(n, end=', ')

    print()

    return


def getCombination(n, r, log=True):
    resultP = 1
    resultR = 1
    resultC = 1
    rnr = r
    logs = []
    for i in range(n, n - r, -1):
        resultP *= i
        resultR *= rnr
        rnr -= 1

    resultC = int(resultP / resultR)

    print(f'resultP : {resultP}')
    print(f'resultR : {resultR}')
    print(f'resultC : {resultC}')
    print(f'{n}C{r} : {resultC}')

    if log:
        for i in range(n):
            logs.append(i + 1)
        getCombinationLog(logs, r)


def getCombinationLog(logs, r):
    logList = list(combinations(logs, r))
    print(f'{len(logs)}P{r} 개수: {len(logList)}')

    for n in logList:
        print(n, end=', ')

    print()

    return


if __name__ == '__main__':
    n = int(input('numN 입력 : '))
    r = int(input('numR 입력 : '))

    getPermutation(n, r)
    getCombination(n, r)
