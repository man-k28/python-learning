# todo:
#   Создайте класс Pet с атрибутам имя, вес и уровень сытости.
#   Напишите метод info, который в качестве результата выдает эти атрибуты.
#   Напишите метод hungry, который возвращает уровень сытости и комментирует: если меньше 5, то «голоден», если больше 10, то «сыт».
#   Напишите метод feed, который передает питомцу некоторую еду, которая прибавляется к уровню сытости и вызывает метод info.

class Eat:
    eatLevel = 0


class Egg(Eat):
    eatLevel = 2


class Apple(Eat):
    eatLevel = 1


class Pet:
    def __init__(self, name, weight, hungry):
        self.__name = name
        self.__weight = weight
        self.__hungry = hungry

    def info(self):
        return dict(self.__dict__.items())

    def hungry(self):
        if self.__hungry < 5:
            print('Want eat')
        elif self.__hungry > 10:
            print('Mne horosho')
        else:
            print('Its ok')

    def feed(self, eat):
        if not isinstance(eat, Eat):
            print('Is not eat!!')
            return
        self.__hungry = self.__hungry + eat.eatLevel


if __name__ == "__main__":
    values = input()
    values = [value for value in values.split(' ')]

    animal = Pet(values[0], int(values[1]), int(values[2]))
    print(animal.info())
    animal.hungry()
    animal.feed(Egg())
    animal.feed(Apple())
    animal.hungry()
