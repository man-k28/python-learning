# Назовем пароль хорошим, если
#
# его длина равна 9 или более символам
# в нем присутствуют большие и маленькие буквы любого алфавита
# в нем имеется хотя бы одна цифра
# Напишите программу, которая требует ввода нового пароля до тех пор, пока не будет введен хороший.
#
#
# На вход программе подается произвольное количество паролей, каждый на отдельной строке. Гарантируется, что среди них присутствует хороший.
#
#
# Для каждого введенного пароля программа должна вывести текст:
#
# LengthError, если длина введенного пароля меньше 9 символов
# LetterError, если в нем все буквы имеют одинаковый регистр
# DigitError, если в нем нет ни одной цифры
# Success!, если введенный пароль хороший
#
# После ввода хорошего пароля все последующие пароли должны игнорироваться.
# Примечание 1. Приоритет вывода сообщений об ошибке в случае невыполнения нескольких условий:
# LengthError, затем LetterError, а уже после DigitError.
#
#
# Sample Input 1:
#
# arr1
# Arrrrrrrrrrr
# arrrrrrrrrrrrrrr1
# Arrrrrrr1
# Sample Output 1:
#
# LengthError
# DigitError
# LetterError
# Success!
#
# Sample Input 2:
#
# beegeek
# Beegeek123
# Beegeek2022
# Beegeek2023
# Beegeek2024
# Sample Output 2:
# LengthError
# Success!

class LengthError(Exception):
    def __str__(self):
        return "LengthError"

class DigitError(Exception):
    def __str__(self):
        return "DigitError"

class LetterError(Exception):
    def __str__(self):
        return "LetterError"

class Success(Exception):
    def __str__(self):
        return "Success!"

if __name__ == "__main__":
    while True:
        try:
            password = input()

            if len(password) < 9:
                raise LengthError()
            elif password.isdigit():
                raise DigitError()
            elif password.islower() or password.isupper():
                raise LetterError()
            elif password.isalpha():
                raise LetterError()
            else:
                raise Success()
        except LengthError as le:
            print(le)
        except DigitError as dig:
            print(dig)
        except LetterError as leter:
            print(leter)
        except Success as su:
            print(su)
            break;