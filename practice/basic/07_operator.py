# 국어, 영어, 수학 점수 입력 후 촘점, 평균, 최고점수 과목, 최저점수 과목과 최고 최저 점수 차이 츨력
import operator

korScore = int(input('국어 점수 입력  : '))
engScore = int(input('영어 점수 입력  : '))
mathScore = int(input('수학 점수 입력  : '))
total = korScore + engScore + mathScore
avg = operator.truediv(total, 3)
print('-' * 30)

maxScore = korScore
minScore = korScore
maxSubject = "국어"
minSubject = "국어"

if maxScore < mathScore:
    maxScore = mathScore
    maxSubject = '수학'
    if maxScore < engScore:
        maxScore = engScore
        maxSubject = '영어'

if minScore > mathScore:
    minScore = mathScore
    minSubject = '수학'
    if minScore > engScore:
        minScore = engScore
        minSubject = '영어'

print(f'총점 : {total}')
print('평균 : %.2f' % avg)
print(f'최고 점수 : {maxSubject}')
print(f'최저 점수 : {minSubject}')
print(f'최고점수 - 최저점수 : {maxScore - minScore}')

print('-' * 30)
