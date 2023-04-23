# todo:
#  Напишите рекурсивную функцию sumn(n), которая вычисляет и печатает сумму чисел от 0 до n.

def summ(n):
    return n[0] + sum(n[1:]) 


n = int(input())

print(summ(range(0, n)))
