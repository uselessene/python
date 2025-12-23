# Рекурсивные функции

# Задание 1. Исполнитель n преобразует число, записанное на экрне
# У исполнителя есть три команды:
# 1. Прибавить 1
# 2. Прибавить 2
# 3. Умножить на 2
"""
def komanda(n, nomer):
    if nomer == 1:
        return n + 1
    if nomer == 2:
        return n + 2
    if nomer == 3:
        return n * 2

def kolvo(start, finish):
    if start > finish:
        return 0
    if start == finish:
        return 1
    return (kolvo(komanda(start, 1), finish) + kolvo(komanda(start, 2), finish) + kolvo(komanda(start, 3), finish))

otvet = kolvo(3, 10) * kolvo(10, 12)

print(kolvo(3, 10))
print(kolvo(10, 12))
print(otvet)
"""

# Задание 2. Исполнитель f преобразует число на экране
# У исполнителя f две команды:
# 1. Прибавь 1
# 2. Сделай нечетное
"""
def komanda(f, nomer):
    if nomer == 1:
        return f + 1
    if nomer == 2:
        return 2 * f + 1

def kolvo(start, finish):
    if start == 26:
        return 0
    if start > finish:
        return 0
    if start == finish:
        return 1
    return (kolvo(komanda(start, 1), finish) + kolvo(komanda(start, 2), finish))
    
print(kolvo(1, 27))
"""

# Задание 3. Исполнитель s преобразует число на экране
# У исполнителя есть две команды:
# 1. Прибавить 1
# 2. Прибавить 2
"""
def komanda(s, nomer):
    if nomer == 1:
        return s + 1
    if nomer == 2:
        return s + 2

def kolvo(start, finish):
    if start == 14:
        return 0
    if start > finish:
        return 0
    if start == finish:
        return 1

    return (kolvo(komanda(start, 1), finish) + kolvo(komanda(start, 2), finish))

otvet = kolvo(2, 9) * kolvo(9, 18)
print(otvet)
"""

# Обработка символьных строк
# Задание 1. Определить длину самой длинной последовательности X
"""
with open("27686.txt", "r") as f:
    n = f.readlines()
max = 0
count = 0

for i in n:
    for symbol in i:
        if symbol == 'X':
            count += 1
            if count > max:
                max = count
        else:
            count = 0
print(max) 
"""

# Задание 2. Максимальное количество идущих подряд символов без XZZY
"""
with open("36037.txt", "r") as f:
    n = f.readlines()
max = 0
count = 0
text = ""

for i in n:
    text += i

for i in range(len(text) - 3):
    if text[i] == 'X' and text[i + 1] == 'Z' and text[i + 2] == 'Z' and text[i + 3] == 'Y':
        if count > max:
            max = count
        count = 3
    else:
        count += 1
        if count > max:
            max = count
print(max)
"""

# Задание 3. Количество групп из идущих подряд не менее 12 символов,
# которые начинаются и заканчиваются буквой E и не содержат других букв E и букв F
"""
with open("46982.txt", "r") as f:
    n = f.readlines()

s = []
for i in n:
    for j in i:
        if j != "":
            s.append(j)
count = 0

for i in range(len(s)):
    if s[i] == "E":
        for j in range(i + 1, len(s)):
            if s[j] == "F":
                break

            if s[j] == "E":
                dlina = j - i + 1
                if dlina >= 12:
                    count = count + 1
                break
print(count)
"""
