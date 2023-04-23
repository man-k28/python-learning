# todo: Создайте функцию, которая принимает два аргумента, год и месяц, и возвращает list comprehension,
# содержащий все даты этого месяца в этом году. Используйте функцию monthrange(year, month) из модуля
# calendar для нахождения числа дней в месяце.

import calendar
import datetime


def printDaysInMonth(month, year):
    day_count = calendar.monthrange(year, month)
    
    return [datetime.date(year, month, day) for day in range(1, day_count[1]+1) if True]

if __name__ == '__main__':
    x = input()
    x = x.split('.')
    print(printDaysInMonth(int(x[0]), int(x[1])))

