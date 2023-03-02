# print("{} * {} = {}".format(2, 1, 2 * 1))
# print("{} * {} = {}".format(2, 2, 2 * 2))
# print("{} * {} = {}".format(2, 3, 2 * 3))
# print("{} * {} = {}".format(2, 4, 2 * 4))
# print("{} * {} = {}".format(2, 5, 2 * 5))
# print("{} * {} = {}".format(2, 6, 2 * 6))
#
# for i in range(1, 7):
#     print("{} * {} = {}".format(2, i, 2 * i))
import random

# for i in range(10):
#     result = 7 * i
#     print(f'7 * {i} = {result}')

# for k in range(100):
#     pass
#
# for h in range(5):
#     print("hi", end="")

# startNum = int(input("반복의 시작 : "))
# endNum = int(input("반복의 끝 : "))
#
# for i in range(startNum, endNum):
#     print(i)

# n = 1
# while n < 10:
#     result = 7 * n
#     print('{} * {} = {}'.format(7, n, result))
#     n += 1

# n = 1
#
# while n <= 100:
#     if n % 2 == 0:
#         print(f'2의 배수 : {n}')
#     elif n % 3 == 0:
#         print(f'3의 배수 : {n}')
#     n += 1

# sum = 0
#
# for i in range(1, 11):
#     sum += i
#
# current = 30
# rotation = 0
# remove = 0.15
#
# while current >= 20:
#     rotation += 1
#     current -= remove
#     # print(f" 구른 횟수 : {rotation} | 현재 바퀴 두께 : {current}")
#
# print(f'앞으로 구를 수 있는 횟수 : {rotation-1}')

# while (True):
#     print("무한루프")

#
# sum = 0
# flag = True
# date = 0
#
# while flag:
#     patient = random.randint(50, 100)  # 하루 독감 환자 수
#     sum += patient
#     date += 1
#     if sum >= 10000:
#         flag = False
#
#     print(f"DAY {date} : 누적 환자 수 : {sum} ")
#
#
# cnt = 0
# for i in range(100):
#     if i % 7 != 0:
#         continue
#
#     print(f"7의 배수 : {i}")
#     cnt += 1
#
# else:
#     print(f'99까지 의 정수 중 7의 배수는 {cnt} 개')

# minNum = 0
#
# for i in range(1, 101):
#     if i % 3 != 0 or i % 7 != 0:
#         continue
#
#     print(f'공배수 : {i}')
#
#     if minNum == 0:
#         minNum = i
# else:
#     print(f'최소 공배수 : {minNum} ')

# num = 0
# while (True):
#     print("Hello Python")
#     num += 1
#     if (num > 10):
#         break


# num = 1
#
# for i in range(1, 10):
#     # print(f'{num} * {i + 1} = {num * (i + 1)}')
#     num = num * (i + 1)
#     if num > 50:
#         print(f" num = {i + 1} , 50 이상의 값 : {num}")
#         break
#
# for i in range(1, 10):
#     for j in range(i):
#         print("*", end='')
#     print()
#
#
# for i in range(10,0,-1):
#     for j in range(i):
#         print("*", end='')
#     print()

for i in range(1, 10):
    for j in range(2, 10):
        print(f'{j} * {i} = {j * i} \t', end='')
    print()
