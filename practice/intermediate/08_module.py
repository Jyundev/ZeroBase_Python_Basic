# 상품 구매 개수에 따른 할인율 적용 프로그램
import CustomModule.discount as dc

cnt = 0
sum = 0

while True:
    select = int(input('상품을 구매 하시겠어요? [1] 구매 [2] 종료 : '))
    if select == 2:
        break
    elif select == 1:
        price = int(input('상품 가격 입력 : '))
        sum += price
        cnt += 1
    else:
        print(f'다시 입력하세요')

discount = dc.getDiscount(cnt)
total = sum * (1 - dc.getDiscount(cnt) * 0.01)

print(f'할인율 : {discount}%')
print(f'합계 : {format(int(total), ",")}원')
