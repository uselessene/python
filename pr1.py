# Шахматы. Нахождение цвета клеток по координатам
"""
x = int(input())
y = int(input())

if x < 1 or x > 8 or y < 1 or y > 8:
    print("net")
else:
    if (x + y) % 2 == 0:
        print("black")
    else:
        print("white")
"""

# Задание 1. Ход шахматного коня
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 < 1 or x1 > 8 or y1 < 1 or y1 > 8 or x2 < 1 or x2 > 8 or y2 < 1 or y2 > 8:
    print("net")
else:
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
        print("mozet")
    else:
        print("ne mozet")
"""

# Задание 2. Сумма четных чисел от k до n
"""
k = int(input("k"))
n = int(input("n"))
sum = 0

for i in range(k, n + 1):
    if i % 2 == 0:
        sum += i
print(sum)
"""

# Задание 3. Сумма введенных чисел
"""
nol = 0
while True:
    num = int(input())
    if num == 0:
        break
    nol += num
print(nol)
"""

# Задание 4. Факториал числа
"""
n = int(input())
factorial = 1
for i in range(1, n + 1):
    facttorial *= i
print(factorial)
"""
