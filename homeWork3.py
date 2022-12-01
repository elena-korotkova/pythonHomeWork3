"""
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8#:~:text=%D0%92%20%D0%BC%D0%B0%D1%82%D0%B5%D0%BC%D0%B0%D1%82%D0%B8%D0%BA%D0%B5%2C%20%D1%87%D0%B8%D1%81%D0%BB%D0%B0%20%D0%BD%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8%20%E2%80%94%20%D0%BE%D1%82%D1%80%D0%B8%D1%86%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%20%D0%B8%D0%BD%D0%B4%D0%B5%D0%BA%D1%81%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%8D%D0%BB%D0%B5%D0%BC%D0%B5%D0%BD%D1%82%D1%8B%20%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D1%87%D0%B8%D1%81%D0%B5%D0%BB%20%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8.)
"""

from random import randint


def getSumOddElements(mas):
    print(mas,' -> ',{sum(mas[1::2])})

def getMult(mas):
    _range = range(int((len(mas) / 2)) + 1) if len(mas) % 2 else range(int((len(mas)/2)))
    print(mas,' -> ',[mas[x] * mas[-(x + 1)] for x in _range])

def getDiffMinMax(mas):
    tmp = [round(x % 1, 10) for x in mas if round(x % 1, 10) != 0]
    print(tmp,' -> ', max(tmp) - min(tmp))

def getDecToBin(num):
    _num=num
    res = []
    while num > 0:
        num, ost = divmod(num, 2)
        res.append(ost)
    res = res[::-1]
    out = 0
    for x in range(len(res)):
       out += res[x] * 10 ** (len(res) - 1 - x)
    print(_num,' -> ',out)

def getFibonachi(num):
    res_pos = []
    res_neg = []
    for n in range(num+1):
        tmp_pos = res_pos[n-2] + res_pos[n-1] if n > 1 else n
        res_pos.append(tmp_pos)
        n *= -1
        tmp_neg = res_neg[abs(n+2)] - res_neg[abs(n+1)] if n < -1 else abs(n)
        res_neg.append(tmp_neg)
    print(num,' -> ',res_neg[::-1] + res_pos[1:])


if __name__ == '__main__':
    getSumOddElements([x for x in range(randint(0, 10))])
    getMult([2, 3, 4, 5, 6])
    getMult([2, 3, 5, 6])
    getDiffMinMax([1.1, 1.2, 3.1, 5, 10.01])
    getDecToBin(45)
    getFibonachi(8)
