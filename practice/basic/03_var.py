# 원의 반지름 입력 하여 넓이와 둘레 길이 출력
# TypeError 발생

# pi = 3.14
# radius = int(input('원의 반지름 입력 : '))
#
# print('원의 넓이 : %d' % int(radius * radius * pi))
# print('원 둘레 길이 : %d' % int(radius * 2 * pi))
# # TypeError: can't multiply sequence by non-int of type 'float'
# print('원의 넓이 : %.1f' % float(radius * radius * pi))
# print('원의 둘레 길이 : %.1f' % float(radius * 2 * pi))
# print('원의 넓이 : %.3f' % float(radius * radius * pi))
# print('원의 둘레 길이 : %.3f' % float(radius * 2 * pi))

# pi = 3.14
# radius = int(input('원의 반지름 입력 : '))
#
# circleArea = radius * radius * pi
# circleLength = radius * 2 * pi
#
# print('원의 넓이 : %d' % circleArea)
# print('원 둘레 길이 : %d' % circleLength)
# print('원의 넓이 : %.1f' % circleArea)
# print('원의 둘레 길이 : %.1f' % circleLength)
# print('원의 넓이 : %.3f' % circleArea)
# print('원의 둘레 길이 : %.3f' % circleLength)
#

# 개인정보 입력 받기
name = input('이름 입력 : ')
mail = input('메일 입력 : ')
id = input('아이디 입력: ')
password = input('패스워드 입력: ')
num1 = input('주민번호 앞자리 입력: ')
num2 = input('주민번호 뒷자리 입력: ')
address = input('주소 입력: ')

print('-' * 20)
print()

print(f'이름 : {name}')
print(f'메일 : {mail}')
print(f'아이디 : {id}')
print('패스워드 : {}'.format('*' * len(password)))
print(f'주민번호  : {num1} - {num2[0]}******')
print(f'주소 : {address}')

print()
print('-' * 20)
