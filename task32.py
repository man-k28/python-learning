#todo: Дан генетический код ДНК (строка, состоящая из букв G, C, T, A)
# Постройте РНК, используя принцип замены букв: G → C, C → G, T → A, A→T.
# Напишите функцию, которая на вход получает ДНК, и возвращает РНК. Например:
# Ввод: GGCTAA
# Вывод: CCGATT

dnk = input()
chars = "GCTA"
rnk = []


for index, symbol in enumerate(dnk):
    if symbol.casefold()  == 'G'.casefold():
        rnk.append('C')
    elif symbol.casefold()  == 'C'.casefold():
        rnk.append('G')
    elif symbol.casefold()  == 'T'.casefold():
        rnk.append('A')
    elif symbol.casefold()  == 'T'.casefold():
        rnk.append('A')
    else:
        rnk.append(symbol)


print(''.join(rnk))