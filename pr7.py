# Олимпиадное программирование
# Задание 1. Возрастающая последовательность
"""
def f(n):
    if n[0] > n[1]:
        return f(n[1:])
    if n[1] >= n[2] and n[2] >= n[3]:
        del n[1]
        return n
n = [6, 2, 5, 4, 2, 5, 6]
print(f(n))
"""

# Задание 2. Наибольшая длина возрастающей последовательности
"""
n = int(input())
k = []

for i in range(n):
    chislo = int(input())
    k.append(chislo)

dlina = [1] * n
for i in range(n):
    for j in range(i):
        if k[j] < k[i]:
            if dlina[j] + 1 > dlina[i]:
                dlina[i] = dlina[j] + 1
print(max(dlina))
"""

# Задание 3. К удивительная
"""
k = 1050
count = 0

for i in range(1, k):
    perev = int(str(i)[::-1])
    if i + perev == k:
        count += 1
print(count)
"""
