#todo:
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны. Напечатайте список дат в 2023 году, когда вход бесплатен.
import calendar
import datetime


if __name__ == '__main__':
    year = int(input())
    for month in range(1, 12):
        print(datetime.date(year, month, calendar.monthcalendar(year, month)[2][4]))