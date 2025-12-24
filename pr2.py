# Двумерные массивы
"""
with open ("39762.txt", "r") as f:
    n = f.readlines()
    n = [int(el) for el in n]
print(n)
"""

# Задание 1
"""
with open ("39762.txt", "r") as f:
    n = f.readlines()
    n = [int(el) for el in n]
count = 0
max_summa = 0
for i in range(len(n) - 1):
    if ((n[i] * n[i + 1]) % 15) == 0 and ((n[i] + n[i + 1]) % 7) == 0:
        count += 1
        if max_summa < n[i] + n[i + 1]:
            max_summa = n[i] + n[i + 1]
print(count, max_summa)
"""

# Задание 2
"""
with open ("68279.txt", "r") as f:
    n = f.readlines()
    n = (int(el) for el in f)
    max_el = 0

    for el in n:
        if str(el)[-3:] == "562":
            if max_el < el:
                max_el = el
    c = 0
    n = []
    max_sum = 0
    for i in range(len(n)-3):
        l = [n[i], n[i + 1], n[i + 2], n[i + 3]]
        l5 = [el for el in l if len(str(el)) == 5]
        lnot5 = [el for el in l if len(str(el)) != 5]
        lcrat3 = [el for el in l if el % 3 == 0]
        lcrat7 = [el for el in l if el % 7 == 0]
        if len(l5) >= l and len(lnot5) >= 2:
            if len (lcrat3) < len(lcrat7):
                if sum(l) > max_el and sum(l) < max_el * 2:
                    c += l
                    if max_sum < sum(l):
                        max_sum = sum(l)
print(c, max_sum)
"""

# Задание 3
"""
with open("40992.txt", "r") as f:
    n = f.readlines()
    n = [int(el) for el in n]
sum = 0
count1 = 0

for i in n:
    if i % 2 == 1:
        sum += i
        count1 += 1
srednee = sum / count1
count = 0
max_summa = 0

for i in range(len(n) - 1):
    if (n[i] % 5 == 0) or (n[i + 1] % 5 == 0):
        if (n[i] < srednee) or (n[i + 1] < srednee):
            count += 1
            s = n[i] + n[i + 1]
            if s > max_summa:
                max_summa = s

print(count, max_summa)
"""
