# todo:
#  Создайте класс Triangle с методом, который при создании объекта проверяет три переменный x, y, z на то,
#  что из них можно составить треугольник. Требования: все числа должны быть больше нуля, сумма любых двух должны быть больше третьего.
class Triangle:
    def __init__(self, x, y, z):
        if x <= 0 or y <= 0 or x <= 0:
            raise Exception('All x, y, z need great 0')
        if x + y < z or x + z < y or y + z < x:
            raise Exception('Values is invalid')
        print('Triangle is correct')


if __name__ == "__main__":
    values = input()
    values = [int(x) for x in values.split(' ')]

    if len(values) != 3:
        print('Invalid arguments')
        exit(1)

    try:
        triangle = Triangle(values[0], values[1], values[2])
    except Exception as e:
        print(e.args)
