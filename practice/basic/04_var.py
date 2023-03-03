# 체중과 신장을 입력하면 BMI지수가 출력되는 프로그램
#
# weight = input('체중 입력(g) : ')
# height = input('신장 입력(cm) : ')
# if weight.isdigit() and height.isdigit():  # 문자열이 숫자 인지 판단
#     weight = int(weight) * 0.1
#     height = int(height) * 0.01
#     print('체중 : %.2fkg' % weight)
#     print('신장 : %.2fm' % height)
#     bmi = weight / (height * height)
#     print('BMI : %.2f' % float(bmi))
# else:
#     print('숫자를 입력하세요.')

# 위치 바꾸기
num1 = 10
num2 = 20
print('num1 : {1} , num2 : {0}'.format(num1, num2))

# 총점과 평균이 출력되는 프로그램
mid = input('중간고사 점수 : ')

if mid.isdigit():
    pass
else:
    print('잘못 입력했습니다.')
    exit()

final = input('기말고사 점수 : ')

if final.isdigit():
    pass
else:
    print('잘못 입력했습니다.')
    exit()

total = int(mid) + int(final)
avg = total / 2
print(f'총점 : {total}, 평균 : {avg} ')
