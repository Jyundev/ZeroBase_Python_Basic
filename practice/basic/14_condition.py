# 상수도 요금 계산기

part = int(input('업종 선택 (1. 가정용, 2. 대중탕용, 3. 공업용 ) : '))
useWater = int(input('사용량 입력 : '))
price = 0
if part == 1:
    price = 540 * useWater
elif part == 2:
    if useWater <= 50:
        price = 820 * useWater
    if useWater <= 300:
        price = 1920 * useWater
    else:
        price = 2400 * useWater
elif part == 3:
    if useWater <= 500:
        price = 240 * useWater
    else:
        price = 470 * useWater
else:
    print('다시 입력해주세요')

print('=' * 30)
print('상수도 요금표')
print('-' * 30)
print('사용량 \t:\t 요금')
print(f'{useWater} \t:\t {format(price,",")}원')
print('=' * 30)
