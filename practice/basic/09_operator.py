# 고도가 60m 씩 올라갈 때마다 기온이 0.8도 내려갈 경우 기온 출력 프로그램 (지면온도 : 29)
#
# baseTemp = 29
# step = 60
# stepTemp = 0.8
#
# height = int(input('고도 입력 : '))
# temp = int(input('지면 온도 : '))
# targetTemp = baseTemp - (height / 60 * stepTemp)
# print(f'고도 {height}의 기온 : {targetTemp}')
#
# 197개의 빵과 152개의 우유를 17명의 학생한테 동일하게 나눠 줄 경우 한명의 학생이 갖게 되는 빵과 우유의 개수와 남은 빵과 우유의 개수 구하기
bread = 197
milk = 152
student = 17

breadCnt = bread / student
milkCnt = milk / student
breadRest = bread % student
milkRest = milk % student

print(f'학생 한명 당 갖게 되는 빵 : {int(breadCnt)}')
print(f'학생 한명 당 갖게 되는 우유 : {int(milkCnt)}')
print(f'남은 우유 : {milkRest}')
print(f'남은 빵 : {breadRest}')
