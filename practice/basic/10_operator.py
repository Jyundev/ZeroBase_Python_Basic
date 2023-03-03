# 백신 접종 대상자 구분 프로그램
# 19세 이하 또는 65세 이상이면 출생 연도 끝자리(4,2,0)에 따른 접종 그렇지 않으면 일정 확인

# age = int(input('나이 입력 : '))
#
# if age <= 19 or age >= 65:
#     endNum = int(input('출생 연도 끝자리 : '))
#     if endNum == 1 or endNum == 6:
#         print('접종 가능 요일 : 월 ')
#     elif endNum == 2 or endNum == 7:
#         print('접종 가능 요일 : 화 ')
#     elif endNum == 3 or endNum == 8:
#         print('접종 가능 요일 : 수 ')
#     elif endNum == 4 or endNum == 9:
#         print('접종 가능 요일 : 목 ')
#     elif endNum == 5 or endNum == 0:
#         print('접종 가능 요일 : 금 ')
# else:
#     print("하반기 일정 확인")

# 길이(mm)를 입력하면 inch로 환산하는 프로그램
byInch = 0.039
lengthMM = int(input('길이(mm) 입력 : '))
lengthInch = lengthMM * byInch

print(f'{lengthMM}mm -> {lengthInch}inch')
