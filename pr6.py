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