# 국어, 영어, 수학, 국사 점수 입력하면 데이터가 출력되는 프로그램

korAvg = 85
engAvg = 82
mathAvg = 89
scienceAvg = 75
historyAvg = 94

kor = int(input('국어 : '))
eng = int(input('영어 : '))
math = int(input('수학 : '))
science = int(input('과학 : '))
history = int(input('국사 : '))

total = kor + math + eng + science + history
totalAvg = total / 5
avgTotal = korAvg + engAvg + mathAvg + scienceAvg + historyAvg

korGap = kor - korAvg
engGap = eng - engAvg
mathGap = math - mathAvg
scienceGap = science - scienceAvg
hisGap = history - historyAvg

print('-' * 30)
print(f'총점 : {total}({avgTotal - total})')
print(
    f'국어 : {kor}({korGap}), 영어 : {eng}({engGap}), 수학 : {math}({mathGap}), 과학 : {science}({scienceGap}), 국사 : {history}({hisGap})')
print('-' * 30)

gap = ''
if korGap > 0:
    gap = '+' * korGap
else:
    gap = '-' * abs(korGap)  # 절대값 만들기

print(f'국어 편차 : {gap}')

if engGap > 0:
    gap = '+' * engGap
else:
    gap = '-' * abs(engGap)  # 절대값 만들기

print(f'영어 편차 : {gap}')

if mathGap > 0:
    gap = '+' * mathGap
else:
    gap = '-' * abs(mathGap)  # 절대값 만들기

print(f'수학 편차 : {gap}')

if scienceGap > 0:
    gap = '+' * scienceGap
else:
    gap = '-' * abs(scienceGap)  # 절대값 만들기

print(f'과학 편차 : {gap}')

if hisGap > 0:
    gap = '+' * hisGap
else:
    gap = '-' * abs(hisGap)  # 절대값 만들기

print(f'국사 편차 : {gap}')
print('-' * 30)
