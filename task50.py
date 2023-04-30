#todo
# Создайте декоратор, которые переводит все текстовые аргументы функции в верхний регистр и возвращает их в виде списка текстовых аргументов.

def processArgs(*args):
    def upper(*args):
        return [arg for arg in args if isinstance(arg, str)]
    print(upper(*args))

if __name__ == '__main__':
    processArgs('sfsf', 3434, 'dd', 5757)
