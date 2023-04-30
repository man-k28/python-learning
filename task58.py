#todo: Создать абстрактный класс Transport (транспорт) содержащий:
# Поля:
# скорость;
# себестоимость перевозки груза;
# стоимость перевозки груза.
# В классе должны быть абстрактные методы:
# метод Cost (без параметров) – вычисление стоимости перевозки груза.
# Метод Info - информация (без параметров), который возвращает строку, содержащую информацию об объекте.
#
# На его основе реализовать дочерние классы:
# Marine - морской транспорт,
# Ground - наземный транспорт.

class Transport:
    speed = 0
    unit_cost = 0
    cost = 0

    def Cost(self):
        pass
    def Info(self):
        self.Cost()
        print(f'Скорость={self.speed} себестоимость перевозки груза={self.unit_cost} стоимость перевозки груза={self.cost}')

class Marine(Transport):
    def __init__(self) -> None:
        self.speed = 50
        self.unit_cost = 5

    def Cost(self):
        self.cost = self.unit_cost * self.speed / 24
        return self.cost

class Ground(Transport):
    def __init__(self) -> None:
        self.speed = 100
        self.unit_cost = 30

    def Cost(self):
        self.cost = self.unit_cost * self.speed / 7 * 1.049 #коэффициен по бензину
        return self.cost


if __name__ == "__main__":
    marine = Marine()
    ground = Ground()
    marine.Info()
    ground.Info()
