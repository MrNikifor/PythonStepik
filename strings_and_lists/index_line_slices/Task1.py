# Вводятся два слова (через пробел в одной строке). Длина первого слова меньше второго.
# Необходимо обрезать второе слово до длины первого и отобразить обрезанное слово на экране.

# Sample Input:
# Hello Balakirev
# Sample Output:
# Balak

# Решение 1
a, b = map(str, input().split())
print(b[0:len(a)])

# Решение 2
# s = input().split()
# print(s[1][:len(s[0])])

# Решение 3
# [print(b[:len(a)]) for a, b in [input().split()]]
# Решение 4
# print((a := input().split())[1][:len(a[0])])

# Решение 5
# [print(c, end='') for a, c in zip(*input().split())]
