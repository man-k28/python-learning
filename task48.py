# todo:
#  Создайте класс Shape, объекты которого имеют атрибуты
#  Colour – строка, например, «Красный», «Синий»;
#  Square – площадь объекта.
#  Создайте несколько методов:
#  1) Установить цвет объекта.
#  2) Запросить цвет объекта и напечатать его.
#  3) Задать площадь объекта.
#  4) Запросить площадь  объекта.
class Shape:
    __colour = ''
    __square = 0

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour):
        self.__colour = colour

    @property
    def square(self):
        return self.__square

    @colour.setter
    def square(self, square):
        self.__square = square


if __name__ == "__main__":
    values = input()
    values = values.split(' ')
    shape = Shape
    shape.colour = values[0]
    shape.square = int(values[1])
    print(f'{shape.colour} {shape.square}')
