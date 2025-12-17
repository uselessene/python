# Задание 1. Число Фибоначчи
"""
N = int(input("N"))
if (N <= 0):
    print("oshibka")
else:
    l = [0, 1]
    
    for i in range(N - 2):
        new = l[0] + l[1]
        l[0] = l[1]
        l[1] = new
    print(new)
"""

# Задание 2. Кузнечик и способы
"""
N = int(input("N"))
if N <= 0:
    print("oshibka")
elif N == 1:
    print("1 sposob")
elif N == 2:
    print("2 sposoba")
elif N == 3:
    print("4 sposoba")
else:
    l = [1, 2, 4]
    for i in range(N - 3):
        new = l[0] + l[1] + l[2]
        l[0] = l[1]
        l[1] = l[2]
        l[2] = new
    print(l[2], "sposobov")
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

puti = [[[] for j in range(len(coins[0]))] for i in range(len(coins))]

for i in range(len(coins)):
    for j in range(len(coins[i])):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            coins[i][j] = coins[i][j] + coins[i][j - 1]
            puti[i][j] = puti[i][j-1] + ["вправо"]
        elif j == 0:
            coins[i][j] = coins[i][j] + coins[i - 1][j]
            puti[i][j] = puti[i-1][j] + ["вниз"]
        else:
            if coins[i - 1][j] > coins[i][j - 1]:
                coins[i][j] = coins[i - 1][j] + coins[i][j]
                puti[i][j] = puti[i-1][j] + ["вниз"]
            else:
                coins[i][j] = coins[i][j - 1] + coins[i][j]
                puti[i][j] = puti[i][j-1] + ["вправо"]

resultat = coins[-1][-1]
put = puti[-1][-1]

print(resultat)
print(put)
"""
