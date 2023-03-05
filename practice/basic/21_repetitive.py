'''
톱니가 각각 A개와 B개의 톱니바퀴가 서로 맞물려 회전할 때,
회전을 시작한 후 처음 맞물린 톱니가 최초로 다시 만나게 될때 까지의 톱니의 수와 각각의 바퀴 회전수를 출력해보자 (단. B는 A보다 크다)
'''

gearA = int(input('GearA 톱니의 수 입력 : '))
gearB = int(input('GearB 톱니의 수 입력 : '))
flag = True
leastNum = 0
aNum = gearA
bNum = gearB
while flag:
    # A의 톱니 수와 서로 최소 공배수가 같을 경우 반복문을 나옴
    if aNum == leastNum:
        flag = False

    print(f'gearA : {aNum}\t gearB : {bNum}')

    aNum += gearA
    if leastNum != bNum:  # 최소 공배수와 B의 톱니 수가 다를 경우에 만 +
        bNum += gearB

    if bNum % gearA == 0:  # 최소 공배수 구하기
        leastNum = bNum

print(f'최초 만나는 톱니 수 : {leastNum}')
print(f'gearA 회전 수 : {leastNum // gearA}')
print(f'gearB 회전 수 : {leastNum // gearB}')
