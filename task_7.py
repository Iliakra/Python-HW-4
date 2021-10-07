""" Красильников Илья
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
начиная с 1! и до n!.
"""


def fact(n):
    range_list = range(1, n+1)
    res = 1
    for num in range_list:
        res *= num
        yield res


g = fact(4)
print(g)

for el in g:
    print(el)