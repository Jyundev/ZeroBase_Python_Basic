# 등비수열 함수

def sequenceFunc(first, step, last):
    val = first
    sum = 0
    for i in range(last):
        if i != 0:
            val *= step

        sum += val
        print(f'{i + 1}번째 항의 값 : {val}')
        print(f'{i + 1}번째 항까지의 합 : {sum}')

    return


first = int(input('a1 입력 : '))
step = int(input('공차 입력 : '))
last = int(input('n 입력 : '))
sequenceFunc(first, step, last)
