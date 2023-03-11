# 공과금 비율 프로그램

import CustomModule.bill as bill

i = int(input('수입 입력 : '))
bill.setIncome(i)
w = int(input('수도 요금 입력 : '))
bill.setWater(w)
e = int(input('전기 요금 입력 : '))
bill.setElectric(e)
g = int(input('가스 요금 입력 : '))
bill.setGas(g)

bill = bill.getUtility()
print(f'공과금 : {format(bill.get("utility"), ",")}원')
print(f'공과금  비율 : {bill.get("utilityPercent")}%')
