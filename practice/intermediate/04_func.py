# 재귀함수를 이용한 팩토리얼
#
# def factorial(n):
#     if n > 1:
#         return n * factorial(n - 1)
#     else:
#         return 1
#
#
# n = int(input('input number : '))
# print(f'factorial : {format(factorial(n),",")}')

# 단리/월복리 계산기 함수

# 단리 계산기
def singleRate(m, t, r):
    yearRate = m * (r * 0.01)
    total = yearRate * t + m
    return format(int(total), ",")


# 월복리 계산기
def multiRate(m, t, r):
    total = m
    for i in range(12 * t):
        total += total * (r / 12 * 0.01)

    return format(int(total), ",")


money = int(input('예치금(월) : '))
term = int(input('기간(년) : '))
rate = int(input('연 이율(%) : '))

print('[단리 계산기]')
print('=' * 15)
print(f'예치금 : {format(money, ",")}')
print(f'예치기간 : {term}')
print(f'연 이율 : {rate}%')
print('-' * 15)
print(f'{term}년 후 총 수령액 : {singleRate(money, term, rate)}')

print('[월복리 계산기]')
print('=' * 15)
print(f'예치금 : {format(money, ",")}')
print(f'예치기간 : {term}')
print(f'연 이율 : {rate}%')
print('-' * 15)
print(f'{term}년 후 총 수령액 : {multiRate(money, term, rate)}')
