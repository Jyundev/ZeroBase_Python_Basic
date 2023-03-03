# 주문 확인서 프로그램
import datetime

name = input('고객 이름 : ')
product = input('상품명 : ')
orderNum = input('주문 번호 : ')
cardOrMoney = input('결재 방법 : ')
price = input('상품 금액 : ')
payMent = input('결재 금액 : ')
point = input('포인트 : ')
data = datetime.datetime.today()
installment = input('할부 : ')

print( )
print(f'{name} 고객님 안녕하세요.')
print(f'{name} 고객님의 주문이 완료되었습니다.')
print('다음은 주문건에 대한 상세 내역입니다.')

print('-' * 25)
print(f'상품명 : {product}')
print(f'주문번호 : {orderNum}')
print(f'결재방법 : {cardOrMoney}')
print(f'상품금액 : {price}')
print(f'결재금액 : {payMent}')
print(f'포인트 : {point}')
print(f'결제일시 : {data}')
print(f'할부 : {installment}')
print('할부유형 : 무')
print('문의  : 02-1234-5678')
