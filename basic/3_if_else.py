# num1 = 10
# num2 = 100
#
# result = True if num1 > num2 else False
# print(f"조건식 결과 : {result}")
# print("num1은 num2 보다 크다.") if num1 > num2 else print("num1은 num2 보다 작다.")
#
# limitSnow = 30
# snow = int(input("적설량 입력(cm) : "))
#
# print(f'적설량(cm) : {snow} -> 대설 경보 발령!!') if snow >= limitSnow else \
#     print(f'적설량(cm) : {snow} -> 대설 경보 해제!!')

# if 10 > 5:
#     print("10은 5보다 크다")
#
# num1 = 23
# num2 = 30
#
# if num1 <= num2:
#     print(f"{num1} <= {num2} : {num1 <= num2}")
# else:
#     print(f"{num1} <= {num2} : {num1 <= num2}")
#
# korScore = int(input("국어 점수 : "))
# engScore = int(input("영어 점수 : "))
# mathScore = int(input("수학 점수 : "))
# avg = (korScore + engScore + mathScore) / 3
#
# if avg >= 90:
#     print('참 잘했어요')
# else:
#     print("노력하세요!")
#
# print('참 잘했어요') if avg >= 90 else print("노력하세요!")
#
# if len("Hello World") > 100:
#     pass #나중에 코딩하겠다는 뜻
# else:
#     pass
#
# floatNum = float(input("소수 입력 : "))
#
# if floatNum - int(floatNum) >= 0.5:
#     print(f"올림 : {int(floatNum + 1)}")
# else:
#     print(f"내림 : {int(floatNum)}")
#
# userPoint = 20
# minAblePoint = 100
# print('포인트 사용 가능') if userPoint >= minAblePoint else print("포인트 사용 불가능")
#
# result = print('포인트 사용 가능') if userPoint >= minAblePoint else '불가능'
# print(f'포인트 사용 가능 여부 : {result}')

# rainPercent = int(input("비올 확률(%) : "))
# # 조건식
# print("우산을 챙기세요") if rainPercent >= 50 else print("양산을 챙기세요")
#
# # if~else
# if rainPercent >= 50:
#     print("우산을 챙기세요")
# else:
#     print("양산을 챙기세요")
#

# examScore = int(input("시험 성적 : "))
# grades = ''
#
# if examScore >= 90:
#     grades = 'A'
# elif examScore >= 80:
#     grades = 'B'
# elif examScore >= 70:
#     grades = 'C'
# elif examScore >= 60:
#     grades = 'D'
# else:
#     grades = 'F'
#
# print(f"성적 : {grades}")

# examScore = int(input("시험 성적 : "))
# grades = ''
#
# if examScore >= 90:
#     grades = 'A'
# elif examScore >= 60 and examScore < 70:
#     grades = 'D'
# elif examScore >= 70 and examScore < 80:
#     grades = 'C'
# elif examScore >= 80 and examScore < 90:
#     grades = 'B'
# else:
#     grades = 'F'
#
# print(f"성적 : {grades}")

# carDisplacement = int(input("자동차 배기량 입력 : "))
# tax = 0
#
# if carDisplacement >= 5000:
#     tax = 600000
# elif carDisplacement >= 4000:
#     tax = 500000
# elif carDisplacement >= 3000:
#     tax = 400000
# elif carDisplacement >= 2000:
#     tax = 300000
# elif carDisplacement >= 1000:
#     tax = 200000
# else:
#     tax = 100000
#
# print(f"배기량 : {carDisplacement} 세금 : {tax}")

# examScore = int(input("시험 성적 : "))
# grades = ''
#
# if examScore >= 90:
#     grades = 'A'
# else:
#     print("재시험 대상입니다.")
#     if examScore >= 80:
#         grades = 'B'
#     elif examScore >= 70:
#         grades = 'C'
#     elif examScore >= 60:
#         grades = 'D'
#     else:
#         grades = 'F'
#
# print(f"성적 : {grades}")

selectNum = int(input('출퇴근 대상자 인가요? 1(YES) 2(NO) : '))
if selectNum == 1:
    print("교통 수단을 선택하세요.")
    print('1. 도보/자전거\n2. 버스/지하철\n3. 자가용')
    tran = int(input('번호 선택 : '))

    if tran == 1:
        print("세금 감면 5%")
    elif tran == 2:
        print("세금 감면 3%")
    elif tran == 3:
        print('세금 감면 1%')
    else:
        print('존재하지 않는 번호입니다.')
elif selectNum == 2:
    print('세금 변동 없습니다.')
else:
    print('잘못 입력했습니다.')
