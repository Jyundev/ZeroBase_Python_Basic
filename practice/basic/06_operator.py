# 상품 가격과 지불 금액을 입력하면 거스름 돈을 계산하는 프로그램
# 단, 거스름돈은 지폐와 동전의 개수를 최소, 1원단위로 절사
productPrice = input('상품 가격 입력 : ')
payPrice = input('지불 금액 : ')
cahrge = 0

if productPrice.isdigit() and payPrice.isdigit():
    if int(productPrice) < int(payPrice):
        charge = int(payPrice) - int(productPrice)
        print('거스름 돈 : %d' % charge)
        print('-' * 20)
        charge50000 = charge / 50000
        charge10000 = (charge % 50000) / 10000
        charge5000 = (charge % 10000) / 5000
        charge1000 = (charge % 5000) / 1000
        charge500 = (charge % 1000) / 500
        charge100 = (charge % 500) / 100
        charge10 = (charge % 100) / 10
        print("5,0000 %d장" % charge50000)
        print(f"1,0000 %d장" % charge10000)
        print(f"5000 %d장" % charge5000)
        print(f"1000 %d장" % charge1000)
        print(f"500 %d장" % charge500)
        print(f"100 %d장" % charge100)
        print(f"10 %d장" % charge10)
        print('-' * 20)
    else:
        print('지불 금액이 모자릅니다.')

else:
    print('숫자를 입력하세요.')
