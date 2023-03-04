# 난수를 이용한 홀/짝 프로그램
# import random
#
# flag = True
#
# while flag:
#     comNum = random.randint(1, 2)
#     # print(comNum)
#     if comNum == 1:
#         comNumStr = '홀'
#     else:
#         comNumStr = '짝'
#
#     select = int(input('홀/짝 선택 1. (홀) 2. (짝) : '))
#     if comNum == select:
#         print(f'빙고 : {comNumStr}')
#         flag = False
#     else:
#         print(f'실패 : {comNumStr}')
import random

# 난수를 이용한 가위 바위 보
flag = True
comNum = random.randint(1, 3)

while flag:
    userResult = ''
    comResult = ''

    print(comNum)
    select = int(input('[가위 | 바위 | 보] 선택 -> 1. 가위 2. 바위  3. 보 : '))
    # 1 > 3 , 2 > 1, 3 > 2

    if comNum == select:
        userResult = '무승부'
        comResult = '무승부'
    elif comNum == 1:
        if select == 2:
            userResult = '승'
            comResult = '패'
            flag = False
        else:
            userResult = '패'
            comResult = '승'
    elif comNum == 2:
        if select == 3:
            userResult = '승'
            comResult = '패'
            flag = False
        else:
            userResult = '패'
            comResult = '승'
    elif comNum == 3:
        if select == 1:
            userResult = '승'
            comResult = '패'
            flag = False
        else:
            userResult = '패'
            comResult = '승'
    else:
        print('다시 입력해 주세요.')

    print(f'컴퓨터 : {comNum}, 유저 : {select}')
    print(f'컴퓨터 : {comResult}, 유저 : {userResult}')
