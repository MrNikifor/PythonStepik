# Подвиг 6. Допишите программу для нахождения числа сочетаний из n по k (значения вводятся в программе), используя формулу .,
# где . Выведите результат в консоль в виде целого числа с помощью функции print.
# Для вычисления факториалов воспользуйтесь соответствующей функцией из библиотеки math.
# Sample Input:
# 6 3
# Sample Output:
# 20

# Рушение 1
import math

n, k = map(int, input().split())

general_factorial = math.factorial(n)/(math.factorial(k) * math.factorial(n - k))
print(int(general_factorial))