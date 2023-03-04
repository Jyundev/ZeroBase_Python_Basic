# '*'를 이용해서 모양 출력
import time

print("#1")
for i in range(5):
    for j in range(i + 1):
        print("*", end='')
    print()
print('-' * 20)

print("#2")
for i in range(5, 0, -1):
    print(' ' * (i - 1), '*' * (6 - i))
print('-' * 20)

print("#3")
for i in range(5):
    for j in range(5 - i):
        print("*", end='')
    print()
print('-' * 20)

print("#4")
for i in range(5, 0, -1):
    print(' ' * (5 - i), '*' * i)
print('-' * 20)

print('#5')
for i in range(1, 10):
    if i > 5:
        i = 10 - i
    for j in range(i):
        print('*', end="")
    print()
print('-' * 20)

print('#6')
for i in range(5, 0, -1):
    print(' ' * (5 - i), '*')

print('-' * 20)

print('#7')
for i in range(5, 0, -1):
    print(' ' * (i - 1), '*')
print('-' * 20)

print('#8')

for i in range(1, 10):
    if i > 5:
        i = 10 - i
    print(' ' * (5 - i), "*" * (2 * i - 1), ' ' * (5 - i))
print('-' * 20)

