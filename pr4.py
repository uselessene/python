# Рекурсивные функции
# Задание 1. Функция факториала числа
"""
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    return 1
print(factorial(8))
"""

# Задание 2. Функция, которая принимает и возвращает согласные буквы
"""
def remove_vowels(string):
    bukvi = "aeiouAEIOU"

    if len(string) == 0:
        return ""
    stroka = string[0]
    srez = string[1:]

    if stroka in bukvi:
        return remove_vowels(srez)
    else:
        return stroka + remove_vowels(srez)
print(remove_vowels("Hello PineApple Apple Pen"))
"""

# Задание 3. Функция вывода строки треугольника Паскаля
"""
def pascal(n):
    if n == 1:
        return [1]
    prev = pascal(n - 1)
    stroka = [1]

    for i in range(len(prev) - 1):
        stroka.append(prev[i] + prev[i + 1])

    stroka.append(1)
    return stroka
print(pascal(10))
"""

# Задание 4. Лабиринт для героя
"""
maze = [
    's----',
    '##---',
    '---##',
    '----x'
]
def solve(m):
    koordinata_x, koordinata_y = 0, 0
    for j in range(len(m)):
        for i in range(len(m[j])):
            if m[j][i] == 's':
                koordinata_x, koordinata_y = i, j

    def robot(i, j, ko):
        if j < 0 or i < 0 or j >= len(m) or i >= len(m[0]):
            return None
        if m[j][i] == '#' or [i, j] in ko:
            return None
        if m[j][i] == 'x':
            return []
        ko = ko + [[i, j]]
        
        otvet = robot(i + 1, j, ko)
        if otvet is not None:
            return ['вправо'] + otvet

        otvet = robot(i, j + 1, ko)
        if otvet is not None:
            return ['вниз'] + otvet

        otvet = robot(i - 1, j, ko)
        if otvet is not None:
            return ['влево'] + otvet

        otvet = robot(i, j - 1, ko)
        if otvet is not None:
            return ['вверх'] + otvet
        return None
    return robot(koordinata_x, koordinata_y, [])
print(solve(maze))
"""
