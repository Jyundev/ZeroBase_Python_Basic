# 1부터 1000까지의 소수인 난수 10개를 생성하되,소수가 아니면 예외가 발생
import random


class NotPrimeException(Exception):
    def __init__(self, n):
        super().__init__(f'{n} is not prime number.')


class PrimeException(Exception):
    def __init__(self, n):
        super().__init__(f'{n} is prime number.')


def isPrime(number):
    isPrime = True

    for i in range(2, number + 1):
        if number % i == 0 and i != number:
            isPrime = False

    if isPrime:
        raise PrimeException(number)
    else:
        raise NotPrimeException(number)


rands = random.sample(range(1, 1000), 10)  # 난수 10개 생성
# rands = [2, 3, 17, 19, 20, 47, 34]
primes = []

for prime in rands:
    try:
        isPrime(prime)
    except NotPrimeException as e:
        print(e)
        continue
    except PrimeException as e:
        print(e)
        primes.append(prime)

print(f'Random Number : {rands}')
print(f'Prime Number : {primes}')
