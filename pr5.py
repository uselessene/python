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

def solve(maze):
    koordinata_x = 0
    koordinata_y = 0
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 's':
                koordinata_x = x
                koordinata_y = y

robottut = []

maze = [
    's----',
    '##---',
    '---##',
    '----x'
]

print(solve(maze))