# def add(n1, n2):
#     print(n1 + n2)
#
#
# def sub(n1, n2):
#     print(n1 - n2)
#
#
# def mul(n1, n2):
#     print(n1 * n2)
#
#
# def div(n1, n2):
#     print(n1 / n2)
#
#
# def calculator(n1, n2):
#     try:
#         add(n1, n2)
#         sub(n1, n2)
#         mul(n1, n2)
#         div(n1, n2)
#     except:
#         print('예상 하지 못한 예외 발생')
#
#
# calculator(10, 0)
#
#
# nums = []
#
# while True:
#     if len(nums) == 5:
#         break
#     try:
#         nums.append(int(input('숫자 입력 : ')))
#     except:
#         print('숫자를 입력하세요')
#
# print(nums)
# nums = []
# n = 1
#
# while n < 6:
#     try:
#         num = int(input('슷자 입력 : '))
#     except:
#         print('예외발생!!')
#         continue
#     else:
#         if num % 2 == 0:
#             nums.append(num)
#             n += 1
#         else:
#             print('홀수입니다.', end='')
#             print('다시 입력하세요')
#             continue
#
# print(nums)
#
# nums = []
# evenList = []
# oddList = []
# floatList = []
#
# while True:
#     if len(nums) > 5:
#         break
#     try:
#         nums.append(float(input('input number : ')))
#     except:
#         print('exception raise!')
#         continue
#
#     else:
#         n = nums[len(nums) - 1]
#         if not n.is_integer():
#             floatList.append(n)
#         elif n % 2 == 0:
#             evenList.append(n)
#         else:
#             oddList.append(n)
#
# print(f'numsLit : {nums}')
# print(f'evenList : {evenList}')
# print(f'oddList : {oddList}')
# print(f'floatList : {floatList}')

# try:
#     inputData = input('input number : ')
#     numInt = int(inputData)
# except:
#     print('exception raise!!')
#     print('not number')
# else:
#     if numInt % 2 == 0:
#         print('even number!')
#     else:
#         print('odd number!')
#
# finally:
#     print(f'inputData : {inputData}')
#
# n = 0
# dataList = []
# evenList = []
# oddList = []
# floatList = []
#
# while True:
#     if n == 5:
#         break
#
#     try:
#         data = input('input number : ')
#         inputNumber = float(data)
#
#     except:
#         print('exception raise!')
#         continue
#     else:
#         n += 1
#         if not inputNumber.is_integer():
#             floatList.append(inputNumber)
#         elif inputNumber % 2 == 0:
#             evenList.append(int(inputNumber))
#         else:
#             oddList.append(int(inputNumber))
#
#     finally:
#         dataList.append(data)
#
# print(f'dataList : {dataList}')
# print(f'evenList : {evenList}')
# print(f'oddList : {oddList}')
# print(f'floatList : {floatList}')

# num1 = int(input('input number1 : '))
# num2 = int(input('input number2 : '))
#
# try:
#     print(f'num1 / num2 ={num1 / num2}')
# except Exception as e:
#     print('0으로 나눌 수 없습니다.')
#     print(f'Exception : {e}')
#
# print(f'num1 * num2 = {num1 * num2}')
# print(f'num1 + num2 = {num1 + num2}')
# print(f'num1 - num2 = {num1 - num2}')

# def divCalaulator(n1, n2):
#     if n2 != 0:
#         print(f'{n1} / {n2} : {n1 / n2}')
#     else:
#         raise Exception('0으로 나눌 수 없습니다.')
#
#
# num1 = int(input('input number1 : '))
# num2 = int(input('input number2 : '))
#
# try:
#     divCalaulator(num1, num2)
# except Exception as e:
#     print(e)

# def sendMessage(message):
#     if len(message) <= 10:
#         raise Exception(f'10글자 이하 SMS 전환 후 발송 : {message}', 1)
#     else:
#         raise Exception(f'10글자 초과 MMS 전환 후 발송 : {message}', 2)
#
#
# message = input('message : ')
#
# try:
#     sendMessage(message)
# except Exception as e:
#     print(e.args[0], " ", e.args[1])

class NotUserException(Exception):

    def __init__(self, num):
        super().__init__(f'{num}은(는) 사용할 수 없습니다.')


def divCalculator(n1, n2):
    if n2 == 0:
        raise NotUserException(n2)
    else:
        print(f'{n1} / {n2} = {n1 / n2}')


num1 = int(input('num1 : '))
num2 = int(input('num2 : '))

try:
    divCalculator(num1, num2)
except Exception as e:
    print(e)
