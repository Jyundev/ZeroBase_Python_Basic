# 모든 배가 입항하는 날짜
# 첫 입항일은 2023년 1월 1일 오전 10시
# 과일 선박 : 3일 주기 / 생선 선박 : 4일 주기 / 야채 선박 : 5일 주기
from datetime import datetime, timedelta


def getCommonDateTerm(d1=3, d2=4, d3=5):
    minMultiple = 0
    for i in range(1, (d1 * d2 * d3) + 1):
        if i % d1 == 0 and i % d2 == 0 and i % d3 == 0:
            minMultiple = i

    return minMultiple


path = "C:/Users/YUN/Python/"
baseTime = datetime(2023, 1, 1, 10, 0, 0)
while True:
    with open(path + 'common_date.txt', 'a') as f:
        if baseTime.month == 1 and baseTime.day == 1:
            f.write(f'{baseTime.year}년 모든 선박 입항일\n')

        f.write(str(baseTime) + '\n')
        baseTime += timedelta(days=getCommonDateTerm())
        # 2024년이 되면 종료
        if baseTime.year == 2024:
            break

with open(path + 'common_date.txt', 'r') as f:
    line = f.readline()
    while line != '':
        print(f'{line}')
        line = f.readline()
