# Работа с таблицами
# Задание 1. Черепашка с путем наоборот
"""
import csv
with open("36031.csv", "r") as f:
    n = list(csv.reader(f))
    l = []
    for i in range(len(n)):
        a = (n[i][0].split(';'))
        a = [int(el) for el in a]
        l.append(a)

coins = l[-1::-1]
for i in range(len(coins)):
    coins[i] = coins[i][-1::-1]
put = []

for i in range(len(coins)):
    for j in range(len(coins[i])):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            coins[i][j] = coins[i][j] + coins[i][j - 1]
            put.append("влево")
        elif j == 0:
            coins[i][j] = coins[i][j] + coins[i - 1][j]
            put.append("вверх")
        else:
            if coins[i - 1][j] > coins[i][j - 1]:
                coins[i][j] = coins[i - 1][j] + coins[i][j]
                put.append("вверх")
            else:
                coins[i][j] = coins[i][j - 1] + coins[i][j]
                put.append("влево")

resultat = coins[i][j]

print(resultat)
print(put)
"""

# Задание 2. Среди семи чисел совпадают четыре числа.
# Среднее значение неповторяющихся чисел больше суммы повторяющихся чисел.
"""
import csv
with open("59778.csv", "r") as f:
    n = list(csv.reader(f))
    l = []

    for i in range(len(n)):
        a = (n[i][0].split(';'))
        a = [int(el) for el in a]
        l.append(a)
    a = l
    count = 0

    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i].count(a[i][j]) == 4:
                repeat = a[i][j]
                x = []
                for j in range(len(a[i])):
                    if a[i][j] not in x and a[i][j] != repeat:
                        x.append(a[i][j])
                summa_repeat = 4 * repeat
                average_sum = sum(x) / 3
                if average_sum > summa_repeat:
                    count += 1
    print(count // 4)
"""

# Задание 3. Максимальная сумма последовательных вещественных чисел
"""
import csv
with open("29666.csv", "r") as f:
    n = list(csv.reader(f))
    l = []
    for i in range(len(n)):
        n[i] = float(n[i][0] + "." + n[i][1])
        l.append(n[i])

max = l[0]
sum = l[0]

for i in range(len(n)):
    if l[i] < l[i - 1]:
       sum += l[i]
    else:
        sum = l[i]

    if sum > max:
        max = sum
print(l)
print(max)
"""
