# 합격 여부 출력 프로그램
def getResultScore(scoreList):
    total = 0
    result = 'Final Pass'
    for score in scoreList:
        total += score
        if score >= 40:
            print(f'{score} : Pass')
        else:
            print(f'{score} : Fail')
            result = 'Final Fail'

    result = 'Final Fail' if total / len(scoreList) < 60 else result
    print(f'총점 : {total}')
    print(f'평균 : {round(total / len(scoreList), 2)}')
    print(f'결과 : {result}')
