# Шахматный конь ходит
# Шахматы. Нахождение цвета клеток по координатам
"""
x = int(input())
y = int(input())

if x < 1 or x > 8 or y < 1 or y > 8:
    print("net")
else:
    if (x + y) % 2 == 0:
        print("Черный")
    else:
        print("Белый")
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
        print("Может")
    else:
        print("Не может")
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

# Динамическое программирование
# Задание 1. Число Фибоначчи
"""
N = int(input())
if (n <= 0):
    print("Ошибка")
else:
    l = [0, 1]

    for i in range(n - 2):
        new = l[0] + l[1]
        l[0] = l[1]
        l[1] = new
    print(new)
"""

# Задание 2. Кузнечик и способы
"""
n = int(input())
if n <= 0:
    print("Ошибка")
elif n == 1:
    print("1 способ")
elif n == 2:
    print("2 способа")
elif n == 3:
    print("4 способа")
else:
    l = [1, 2, 4]
    for i in range(n - 3):
        new = l[0] + l[1] + l[2]
        l[0] = l[1]
        l[1] = l[2]
        l[2] = new
    print(l[2], "способов")
"""

# Задание 3. Черепашка и монеты
"""
coins = [[0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 40, 70, 0, 0, 1],
        [100, 0, 0, 0, 0, 1]]

for i in range(len(coins)):
    for j in range(len(coins[i])):
        if i == 0 and j == 0:
            continue
        elif i == 0 and j != 0:
            coins[i][j] = coins[i][j] + coins[i][j - 1]
        elif i != 0 and j == 0:
            coins[i][j] = coins[i][j] + coins[i - 1][j]
        else:
            coins[i][j] = max(coins[i - 1][j], coins[i][j - 1]) + coins[i][j]

resultat = coins[len(coins)-1][len(coins[0])-1]
print(resultat)
"""

# Задание 3.1. Черепашка и монеты с своим массивом
"""
coins = [[0, 0, 1, 0, 0, 2],
        [2, 0, 100, 1, 0, 1],
        [10, 0, 0, 80, 0, 1],
        [1, 0, 8, 20, 1, 1]]

for i in range(len(coins)):
    for j in range(len(coins[i])):
        if i == 0 and j == 0:
            continue
        elif i == 0 and j != 0:
            coins[i][j] = coins[i][j] + coins[i][j - 1]
        elif i != 0 and j == 0:
            coins[i][j] = coins[i][j] + coins[i - 1][j]
        else:
            coins[i][j] = max(coins[i - 1][j], coins[i][j - 1]) + coins[i][j]

resultat = coins[len(coins)-1][len(coins[0])-1]
print(resultat)
"""

# Задание 3.2. Черепашка и монеты с выводом пцти
"""
coins = [[0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 40, 70, 0, 0, 1],
        [100, 0, 0, 0, 0, 1]]
put = []

for i in range(len(coins)):
    for j in range(len(coins[i])):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            coins[i][j] = coins[i][j] + coins[i][j - 1]
            put.append("вправо")
        elif j == 0:
            coins[i][j] = coins[i][j] + coins[i - 1][j]
            put.append("вниз")
        else:
            if coins[i - 1][j] > coins[i][j - 1]:
                coins[i][j] = coins[i - 1][j] + coins[i][j]
                put.append("вниз")
            else:
                coins[i][j] = coins[i][j - 1] + coins[i][j]
                put.append("вправо")

resultat = coins[i][j]

print(resultat)
print(put)
"""
