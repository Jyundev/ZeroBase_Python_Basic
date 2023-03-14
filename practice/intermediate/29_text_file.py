# 두 개의 수를 입력하면 공약수를 텍스트 파일에 작성

path = "C:/Users/YUN/Python/"


# 공약수
def commonDivisor(n1, n2):
    divisors = []
    for i in range(1, n2):
        if n1 % i == 0 and n2 % i == 0:
            divisors.append(i)
    return divisors


# 최대공약수
def maxCommonDivisor(n1, n2):
    max = 0
    for i in range(1, n2):
        if n1 % i == 0 and n2 % i == 0:
            if max < i:
                max = i
    return max


n1 = int(input('1보다 큰 정수 입력 : '))
n2 = int(input('1보다 큰 정수 입력 : '))

if n1 > 1 and n2 > 1:
    with open(path + 'common_divisor.txt', 'a') as f:
        f.write(f'{n1}와 {n2}의 최대공약수 : {maxCommonDivisor(n1, n2)}\n')
        print('common factor write complete')
else:
    print('1보다 큰 수를 입력하세요')

with open(path + 'common_divisor.txt', 'r') as f:
    line = f.readline()
    while line != '':
        print(f'{line}')
        line = f.readline()
