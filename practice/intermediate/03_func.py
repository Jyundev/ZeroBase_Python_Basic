# 비행기 티켓 영수증 출력 함수

def printTicket(c, i, a, cd, id, ad):
    cp = c * 18000
    dcp = cd * 18000 * 0.5
    ip = i * 25000
    dip = id * 25000 * 0.5
    ap = a * 50000
    dap = ad * 50000 * 0.5
    price = cp + dcp + ip + dip + ap + dap

    print('=' * 30)

    print(f'유아 {c}명 요금 : {int(cp)}')
    print(f'유아 할인 대상 {cd}명 요금 : {int(dcp)}')
    print(f'소아 {i}명 요금 : {int(ip)}')
    print(f'소아 할인 대상 {id}명 요금 : {int(dip)}')
    print(f'성인 {a}명 요금 : {int(ap)}')
    print(f'성인 할인 대상 {ad}명 요금 : {int(dap)}')

    print('=' * 30)

    print(f'Total : {c + i + a + cd + id + ad}')
    print(f'Total Price : {format(int(price), ",")}')

    print('=' * 30)

    return


childPrice = int(input('유아 입력 : '))
disChildPrice = int(input('할인 대상 유아 입력 : '))
infantPrice = int(input('소아 입력 : '))
disInfantPrice = int(input('할인 대상 소아 입력 : '))
adultPrice = int(input('성인 입력 : '))
disAdultPrice = int(input('할인 대상 성인 입력 : '))
printTicket(childPrice, infantPrice, adultPrice, disChildPrice, disInfantPrice, disAdultPrice)
