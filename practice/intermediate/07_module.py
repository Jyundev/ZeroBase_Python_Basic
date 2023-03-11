# 합격 여부 출력 프로그램

import CustomModule.printResult as pr

scoreList = []
for i in range(5):
    score = int(input(f'과목{i + 1} 점수 입력 :'))
    scoreList.append(score)

pr.getResultScore(scoreList)
