
#Zad 1
A = [1 - x for x in range(1, 11)]
B = [4**y for y in range(8)]
C = [z for z in B if z % 2 == 0]
print(A)
print(B)
print(C)
print('')

#Zad 2
import random

list1 = [random.randrange(100) for n in range(10)]
list2 = [number for number in list1 if number % 2 == 0]
print(list1)
print(list2)
print('')

#Zad 3
products = {'ser': 'dag', 'bulka': 'sztuki', 'mieso': 'kg', 'maslo': 'sztuki', 'twarog': 'sztuki'}
products_szt = {key: value for key, value in products.items() if value == 'sztuki'}
print(products)
print(products_szt)
print('')

#Zad 4
def is_right_triangle(a, b, c):
    sum = 0
    if max(a, b, c) == a:
        sum += a * a
    else:
        sum -= a * a
    if max(a, b, c) == b:
        sum += b * b
    else:
        sum -= b * b
    if max(a, b, c) == c:
        sum += c * c
    else:
        sum -= c * c
    if (sum == 0):
        return 1
    else:
        return 0

print(is_right_triangle(3, 4, 5))
print(is_right_triangle(1, 6, 8))
print('')

#Zad 5
def trapezoid_area(a = 2, b = 4, h = 3):
    return (a + b) * h / 2

print(trapezoid_area())
print(trapezoid_area(7, 2, 11))
print('')

#Zad 6
def sequence_product(a1 = 1, b = 4, ile = 10):
    product = 1
    for n in range(ile):
        product *= a1 * b**n
    return product

print(sequence_product())
print(sequence_product(2, 3, 6))
print('')

#Zad 7
def sequence_product2(* an):
    if len(an) == 0:
        return 0
    else:
        product = 1
        for i in an:
            product *= i
        return product

print(sequence_product2(1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144))
print(sequence_product2(2, 6, 18, 54, 162, 486))
print('')

#Zad 8
def shopping_cost(** products):
    print('Na liscie zakupow jest {} produktow'.format(len(products)))
    cost = 0
    for i in products:
        cost += products[i]
    return cost

print(shopping_cost(maslo = 7.99, mleko = 4.99, sok = 4.69, cheddar = 12.49, chleb = 3.90))

#Zad 9
import math
number = float(input("Podaj nieujemna liczbe: "))
try:
    result = math.sqrt(number)
    print(result)
except ValueError:
    print('\nNie mozna obliczyb pierwiastka z liczby ujemnej!\n')
