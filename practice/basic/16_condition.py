# 난수 맞추기 게임
# import random
#
# randNum = random.randint(1, 1000)
#
# flag = True
# cnt = 0
# while flag:
#     cnt += 1
#     num = int(input('1에서 1000까지 정수 입력 : '))
#     if num > randNum:
#         print("더 작은 수 입력")
#     elif num < randNum:
#         print('더 큰 수 입력')
#     else:
#         print(f'빙고!\n난수 : {randNum}, 시도 횟수 : {cnt}')
#         flag = False

# 실내온도 입력하면 자동으로 에어컨 상태가 설정 되는 프로그램

airconState = ''
temp = int(input('실내온도 입력 : '))
if temp <= 18:
    airconState = 'off'
elif temp <= 22:
    airconState = '매우 약'
elif temp <= 24:
    airconState = '약'
elif temp <= 26:
    airconState = '중'
elif temp <= 28:
    airconState = '강'
else:
    airconState = '매우 강'

print(f'에어컨 상태 : {airconState} ')
