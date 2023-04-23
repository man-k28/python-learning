#todo: Напишите программу, в которой используется две функции. В одной программа «спит» 2 секунды, в другой – 3 секунды. Пусть каждая функция возвращает время, которое она «проспала».
# Главная программа запускает цикл от 0 до 10, если число четное, то запускает функцию с 2 секундами, если нечетное, то функцию с 3 секундами. Накапливает сон обеих функций отдельно и печатает две суммы.
import time

def sleeping(seconds):
    start = time.time()
    time.sleep(seconds)
    end = time.time()
    return int(end - start)

if __name__ == '__main__':
    twoCounter = 0
    threeCounter = 0

    for number in range(0,10):
        if number % 2 == 0:
            twoCounter = twoCounter + sleeping(2)
        else:
            threeCounter = threeCounter + sleeping(3)
        print('Two counter seconds: ', twoCounter, ' Three counter seconds: ', threeCounter)
    