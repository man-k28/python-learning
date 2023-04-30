#todo: Задача 1 Переопределите метод __str__, чтобы в нем печатались все атрибуты объекта и их значения через запятую. Например:
# def __init__(self):
#     self.x = 0
#     self.y = 1
#
# Должно быть напечатано x:0, y:1

class Foo:
    def __init__(self):
        self.x = 0
        self.y = 1

    def __str__(self):
        res = [f'{attr}:{value} ' for attr, value in self.__dict__.items()]
        return ''.join(res)


if __name__ == "__main__":
    foo = Foo()
    print(foo)
