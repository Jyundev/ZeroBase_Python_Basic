# 다음과 같이 출력 될 수 있도록 이동거리와 이동시간을 반환하는 함수를 만들어 보자
import math


# def getDistance(s, h, m):
#     return s / 60 * m + s * h
#
#
# s = float(input('속도(km/h) 입력 : '))
# h = float(input('시간(h) 입력 : '))
# m = float(input('시간(m) 입력 : '))
# d = getDistance(s, h, m)
# print(f'{s}(km/h) 속도로 {h}(h)시간 {m}(m)분 동안 이동한 거리 : {d}(km)')
#

# 이동거리 이동시간 반환 함수
def getTime(speed, distance):
    time = distance / speed
    hour = int(time)
    min = (time - hour) * 60
    times = [hour, min]
    return times


s = float(input('속도(km/h) 입력 : '))
d = float(input('거리 입력 : '))
t = getTime(s, d)
print(f'{s}(km/h) 속도로 {d}(km) 이동한 시간 : {t[0]}시간 {math.trunc(t[1])}분')
