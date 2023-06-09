# todo: Десериализация
# Напишите программу, которая принимает на вход название JSON файла, десериализует содержащийся в этом файле объект и выводит его.
#
# если файла с данным названием нет в папке с программой, программа должна вывести текст:
# Файл не найден
# если файл с данным названием содержит некорректные данные (то есть не удовлетворяющие формату JSON), программа должна вывести текст:
# Ошибка при десериализации
#
# На вход программе подается название JSON файла.
#
#
# Программа должна десериализовать объект, содержащийся в файле с введенным названием, и вывести его. Если при поиске файла или десериализации его содержимого произошла ошибка, программа должна вывести соответствующий текст.
#
# Примечание 1. Название подаваемого файла уже содержит расширение.
#
# Примечание 2. Тестируемый файл numbers.json имеет следующее содержание
#
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# numbers.json
# Sample Output 1:
#
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#
# Ошибка при десериализации

import json
import os


if __name__ == "__main__":
    filename = input()

    if filename.endswith('.json'):
        print('Название подаваемого файла уже содержит расширение.')
        exit(1)

    filename = filename + '.json'

    if not os.path.exists(filename):
        print('Файл не найден.')
        exit(1)

    
    with open(filename, "r") as file:
        try:
            jsonData = json.load(file)
            print(json.dumps(jsonData))
        except Exception as e:
            print(e)
        
        file.close()