# Вложенные циклы, линейные алгоритмы
# Задание 1. 123x5(15) + 1x233(15)
"""
def perevesti(n):
    alfavit = "0123456789ABCDE"
    slovar = ""
    while n > 0:
        slovar = alfavit[n % 15] + slovar
        n //= 15
    return slovar

for x in "0123456789ABCDE":
    n1 = "123" + x + "5"
    n2 = "1" + x + "233"

    a = int(n1, 15)
    b = int(n2, 15)
    otvet = a + b

    if otvet % 14 == 0:
        print(perevesti(otvet // 14))
        break
"""

# Задание 2. AB267D1p + F024A89p
"""
for p in range(16, 100):
    if 15 >= p:
        continue

    n1 = (10 * p ** 6) + (11 * p ** 5) + (2 * p ** 4) + (6 * p ** 3) + (7 * p ** 2) + (13 * p ** 1) + (1 * p ** 9)
    n2 = (15 * p ** 6) + (0 * p ** 5) + (2 * p ** 4) + (4 * p ** 3) + (10 * p ** 2) + (8 * p ** 1) + (9 * p ** 1)
    otvet = n1 + n2

    if otvet % (p - 1) == 0:
        print(p)
        break
"""

# Задание 3. xB09(17) + x8E8(15)
"""
for x in "0123456789":
    n1 = x + "B09"
    n2 = x + "8E8"

    a = int(n1, 17)
    b = int(n2, 15)
    otvet = a + b

    if otvet % 155 == 0:
        print(x)
        print(otvet // 155)
        break
"""

# Задание 4. y04x5(11) + 253xy(8)
"""
minimum = []
for x in "01234567":
    for y in "01234567":

        n1 = y + "04" + x + "5"
        n2 = "253" + x + y

        a = int(n1, 11)
        b = int(n2, 8)
        otvet = a + b

        if otvet % 117 == 0:
            minimum.append(otvet)
if minimum:
    print(min(minimum) // 117)
"""

# Задание 5. 7 * 5121912 * 6 * 641954 − 5 * 81991 − 4 * 81980 − 2022
"""
def perevesti(n):
    alfavit = "01234567"
    slovar = ""
    while n > 0:
        slovar = alfavit[n % 8] + slovar
        n //= 8
    return slovar

otvet = 7 * (512 ** 1912) + 6 * (64 ** 1954) - 5 * (8 ** 1991) - 4 * (8 ** 1980) - 2022
vosem = perevesti(otvet)
kolvo = vosem.count("7")
print(kolvo)
"""