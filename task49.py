# todo:
#  Определите класс Person. В конструктор которого передается фамилия и возраст ('Иванов', 29)
#  Реализуйте через магические методы условие, при котором возраст у объекта не будет меняться после инициализации.
class Person:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, attr, value):
        if attr == 'age' and self.age != 0:
            return
        else:
            self.__dict__[attr] = value


if __name__ == "__main__":
    values = input()
    values = values.split(' ')

    person = Person(values[0], int(values[1]))
    print(f'{person.name} {person.age}')
    person.age = 55
    print(f'{person.name} {person.age}')
    person2 = Person(values[0], int(values[1]))
    person2.age = 33
    print(f'{person.name} {person.age}')
