# Вводится стоимость книги X рублей (например, X = 435.78) - положительное вещественное число с точностью до сотых
# (два знака после запятой). Требуется определить, является ли дробное значение (число после запятой) больше 50.
# На экран вывести True, если больше и False - в противном случае.
# Задача делается без использования условного оператора.

# Sample Input:
# 456.56
# Sample Output:
# True

# Решение 1
x = float(input())
x = (x % 1) * 100
x = (int(x) // 1)
print(x > 50)

# Решение 2
# a = float(input())
# print(round(a))

# Решение 3
# print(int(input().split('.')[1]) > 50)