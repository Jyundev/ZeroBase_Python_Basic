import random


def numbers():
    num = random.sample(range(1, 100), 6)
    print(f'로또 번호 : {num}')
