#todo:
# Определите класс Person. При создании объекта p=Person(‘Иванов’, ‘Михаил’, ‘Федорович’) необходимо ввести полное имя человека.
# При печати объекта должно выводиться следующее:
# print(p) # чивородеФлиахиМвонавИ
class Person:
    __first_name = ''
    __lastName = ''
    __second_name = ''

    def __init__(self, first_name, last_name, second_name):
        self.__first_name = first_name
        self.__second_name = second_name
        self.__lastName = last_name

    def __str__(self):
        res = [f'{attr}:{value} ' for attr, value in self.__dict__.items()]
        return self.__second_name[::-1] + self.__lastName[::-1] + self.__first_name[::-1] 


if __name__ == '__main__':
    print(Person('Иванов', 'Михаил', 'Федорович'))