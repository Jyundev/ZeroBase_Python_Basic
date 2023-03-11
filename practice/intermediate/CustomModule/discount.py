# 상품 구매 개수에 따른 할인율 적용 프로그램
def getDiscount(cnt):
    discount = 0
    if cnt >= 5:
        discount = 25
    elif cnt >= 4:
        discount = 20
    elif cnt >= 3:
        discount = 15
    elif cnt >= 2:
        discount = 10
    elif cnt >= 1:
        discount = 5
    else:
        discount = 0
    return discount


if __name__ == '__main__':
    print('실행 파일 에서 실행해 주세요')
