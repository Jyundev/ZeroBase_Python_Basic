# 사용자가 입력한 숫자의 약수를 텍스트 파일에 기록
# def divisor(num):
#     divisors = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             divisors.append(i)
#
#     return divisors
#
#
# path = "C:/Users/YUN/Python/"
#
# n = int(input('0보다 큰 정수 입력 : '))
# if n > 0:
#     with open(path + 'divisor.txt', 'a') as f:
#         f.write(f'{n}의 약수 : {divisor(n)}\n')
#         print('divisor write complete')
# else:
#     print('0보가 큰 수를 입력하세요')
#
# with open(path + 'divisor.txt', 'r') as f:
#     line = f.readline()
#     while line != '':
#         print(f'{line}')
#         line = f.readline()


# 사용자가 입력한 숫자의 소수를 텍스트 파일에 기록

def isPrime(num):
    primes = []
    for i in range(2, num):
        isFlag = True
        for j in range(2, i):
            if i % j == 0:
                isFlag = False
                break

        if isFlag:
            primes.append(i)
    return primes


path = "C:/Users/YUN/Python/"

n = int(input('0보다 큰 정수 입력 : '))
if n > 0:
    with open(path + 'primes.txt', 'a') as f:
        f.write(f'{n}까지의 소수 : {isPrime(n)}\n')
        print('prime write complete')
else:
    print('0보가 큰 수를 입력하세요')

with open(path + 'primes.txt', 'r') as f:
    line = f.readline()
    while line != '':
        print(f'{line}')
        line = f.readline()
