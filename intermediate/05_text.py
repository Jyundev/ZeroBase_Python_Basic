# path = "C:/Users/YUN/Python/pythontxt.txt"
# file = open(path, 'w')
# strCnt = file.write('Hello World')
# print(f'strCnt : {strCnt}')
# file.close()
# import time
#
# path = "C:/Users/YUN/Python/current_time.txt"
#
# lt = time.localtime()
# file = open(path, 'w')
# str = '[' + str(lt.tm_year) + '년 ' + str(lt.tm_mon) + '월 ' + str(lt.tm_mday) + '일]' \
#                                                                                 'python study'
# file.write(str)
# file.close()
# import time
#
# path = "C:/Users/YUN/Python/current_time.txt"
# file = open(path, 'w')  # 'w' 덮어쓰기, 'r' 읽기, 'a' 이어쓰기
# dateStr = time.strftime('[ %y-%m-%d %p %I(%H):%M  ]')
# file.write(dateStr)
# file = open(path, 'r')  # 'w' 덮어쓰기, 'r' 읽기, 'a' 이어쓰기
# str = file.read()
# print(str)
# file.close()
#
# path = "C:/Users/YUN/Python/test.txt"
#
# file = open(path, 'w')
# file.write('Python은 1991년 네덜란드계 소프트웨어 엔지니어인 \
# 귀도 반 로섬이 발표한 고급 프로그래밍 언어로, 플랫폼에 독립적이며 \
# 인터프리터식, 객체지향적, 동적 타이핑(dynamically typed) 대화형 언어이다.\
# Python이라는 이름은 귀도가 좋아하는 코미디인〈Monty Python\'s Flying Circus〉에서 따온 것이다')
# file.close()
#
# file = open(path, 'r')
# str = file.read()
# print(str)
# str = str.replace('Python', '파이썬', 2)
# print(str)
# file.close()
#
# file = open(path, 'w')
# file.write(str)
# file.close()
#
# path = "C:/Users/YUN/Python"
# # 'w' 모드
# file = open(path + '/hello.txt', 'w')
# file.write('Hello World')
# file.close()
#
# # 'a' 모드
# file = open(path + '/hello.txt', 'a')
# file.write('\n I love Python')
# file.close()
#
# # 'x' 모드 FileExistsError
# # file = open(path + '/hello.txt', 'x')
# # file.write('\n I love Python')
# # file.close()
# #
# # 'r' 모드
# file = open(path + '/hello.txt', 'r')
# str = file.read()
# print(str)
#
# def writePrimeNumber():
#     path = "C:/Users/YUN/Python"
#     file = open(path + '/prime.txt', 'a')
#     number = int(input('input numbers : '))
#
#     for i in range(2, number + 1):
#         flag = True
#
#         for j in range(2, i):
#             if i % j == 0 and i != j:
#                 flag = False
#         if flag:
#             file.write(str(i))
#             file.write(str('\n'))
#
#
# def readFile():
#     path = "C:/Users/YUN/Python"
#     file = open(path + '/prime.txt', 'r')
#     print('Primes Number\n' + file.read())
#
#
# writePrimeNumber()
# readFile()
# import random
#
# path = "C:/Users/YUN/Python/"
#
#
# file = open(path + 'asWith.txt', 'a')
# file.write('python study')
# file.close()
#
# file = open(path + '/asWith.txt', 'r')
# str = file.read()
# print(str)
# file.close()
#
# with open(path + '/asWith.txt', 'a') as f:
#     f.write('\nUse As ~ With')
#
# with open(path + 'asWith.txt', 'r') as f:
#     print(f.read())
import random

path = "C:/Users/YUN/Python/"

#
# def lottoNumber(nums):
#     for idx, num in enumerate(nums):
#         with open(path + 'Lotto.txt', 'a') as f:
#             if idx < len(nums) - 2:
#                 f.write(str(num) + ', ')
#             elif idx == len(nums) - 2:
#                 f.write(str(num) + '\n')
#             else:
#                 f.write('bonus : ' + str(num))
#     with open(path + 'Lotto.txt', 'r') as f:
#         print(f.read())
#
#
# nums = random.sample(range(1, 46), 7)
# lottoNumber(nums)
# languages = ['c/c++', 'java', 'python', 'kotlin', 'c#']
# for item in languages:
#     with open(path + 'languages.txt', 'a') as f:
#         f.write(item)
#         f.write('\n')
#
# languages = ['c/c++', 'java', 'python', 'kotlin', 'c#']
# with open(path + 'languages_line.txt', 'a') as f:
#     f.writelines(item + '\n' for item in languages)
#     print(languages, file=f) #리스트로 출력
#
# with open(path + 'languages.txt', 'r') as f:
#     lanList = f.readlines()
#
# print(f'lanList : {lanList}')
# print(f'lanList Type : {type(lanList)}')
#
# with open(path + 'languages.txt', 'r') as f:
#     line = f.readline()
#
#     while line != '':
#         print(f'line : {line}', end='')
#         line = f.readline()

# scoreDic = {}
#
# with open(path + 'scores.txt', 'r') as file:
#     line = file.readline()
#     while line != '':
#         num = line.find(':')
#         item = line[:num]
#         try:
#             key = int(line[num:])
#         except:
#             key = int(line[num + 1:])
#
#         scoreDic.update({item: key})
#         line = file.readline()
#
# print(scoreDic)
scoreDic = {}

with open(path + 'scores.txt', 'r') as file:
    line = file.readline()
    while line != '':
        scoreList = line.split(':')
        item = scoreList[0]
        key = int(scoreList[1].strip('\n'))
        scoreDic[item] = key
        line = file.readline()

print(scoreDic)
