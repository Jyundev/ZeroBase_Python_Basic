# 로또 모듈 프로그램
import random


# Expected type 'Iterable' (matched generic type 'Iterable[_T]'), got 'None' instead
# TypeError: 'NoneType' object is not iterable

def getLottoResult(numbers: list):
    bonus = random.randint(1, 45)
    lottos: list = []
    # noinspection PyTypeChecker
    # if lottos is None or len(lottos) == 0:
    lottos = list(random.sample(range(1, 46), 6))
    finalList = lottos.copy()
    finalList.append(numbers)

    # for n in numbers:
    #     for lotto in lottos:
    #         if n == lotto:
    #             corrects.append(n)
    corrects = list(set(numbers) & set(lottos))

    if len(corrects) == 6:
        print('1등 당첨')
        print(f'번호 : {corrects}')
    elif len(corrects) == 5 and bonus in numbers:
        print('2등 당첨')
        print(f'번호 : {corrects} 보너스 : {bonus}')
    elif len(corrects) == 5:
        print('3등 당첨')
        print(f'번호 : {corrects}')
    elif len(corrects) == 4:
        print('4등 당첨')
        print(f'번호 : {corrects}')
    elif len(corrects) == 3:
        print('5등 당첨')
        print(f'번호 : {corrects}')
    else:
        print('꽝!')
        print(f'기계 번호 : {lottos}')
        print(f'보너스 번호 : {bonus}')
        print(f'선택 번호 : {numbers}')
        print(f'일치 번호 : {corrects}')

    return
