# 교통 과속 프로그램
speed = int(input('속도 입력 : '))
if speed <= 50:
    print('안전 속도 준수!')
else:
    print('안전 속도 위반!')

# 문자메시지 길이에 따라 문자 요금이 결정되는 프로그램
message = input('메시지 입력 : ')
print('--전송 중--')
messageLength = len(message)

print(f'메시지 길이 :{len(message)}')
if messageLength <= 50:
    print('메시지 발송 요금 : 50')
else:
    print('메시지 방송 요금 : 100원')
