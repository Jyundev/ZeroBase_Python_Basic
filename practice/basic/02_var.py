# 사용자가 입력한 데이터의 길이를 출력하는 프로그램
message = input('메시지 입력 : ')
print(f'메시지 문자열 길이 : {len(message)}')

# 다음 문자열에서 '객체지향' 문자열을 찾아보자
article = '파이썬(영어: Python)은 1991년 프로그래머인 귀도 반 로섬이 발표한 고급 프로그래밍 언어로, ' \
          '플랫폼에 독립적이며 인터프리터식, 객체지향적, 동적 타이핑(dynamically typed) 대화형 언어이다. ' \
          '파이썬이라는 이름은 귀도가 좋아하는 코미디 〈Monty Python\'s Flying Circus〉에서 따온 것이다.'

findStr = '객체지향'
print(f'{findStr} 문자열 위치 : {article.find(findStr)}')

# 삼각형의 넓이 구하기
width = float(input('가로 길이 : '))
height = float(input('세로 길이 : '))
print(f'사각형 넓이 : {width * height}')
print(f'삼각형 넓이 : {width * height / 2}')
