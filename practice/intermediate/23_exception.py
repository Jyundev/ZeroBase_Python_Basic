# 총 구매 내역 프로그램

items = {'딸기': 2000, '바나나': 1500, '귤': 500, '메론': 3000, '사과': 1300}
errors = {}

total = 0
cnt = 0
for key in items.keys():
    try:
        cnt = input(f'{key} 구매 개수 : ')
        total += (int(cnt) * items[key])
    except Exception as e:
        errors[key] = cnt
      #  print(e)
        continue

print('-' * 30)
print(f'총 구매 금액 : {total}원')
print('-' * 12, '미결제 항목', '-' * 12)

for k in errors:
    print(f'상품 : {k} | 구매 개수 : {errors[k]}')
