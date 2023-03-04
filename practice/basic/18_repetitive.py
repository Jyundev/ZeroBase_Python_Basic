# 1부터 사용자가 입력한 정수까지의 합, 홀수의 합 그리고 팩토리얼을 출력하는 프로그램

sum = 0
oddSum = 0
evenSum = 0
factorial = 1
num = int(input('정수 입력 : '))
for i in range(1, num + 1):
    sum += i
    factorial = factorial * i
    if i % 2 == 0:
        evenSum += i
    else:
        oddSum += i

print(f'합 : {sum}')
print(f'홀수 합 : {oddSum}')
print(f'짝수 합 : {evenSum}')
print(f'팩토리얼 결과 :{format(factorial, ",")}')
