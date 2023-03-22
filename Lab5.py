<<<<<<< HEAD
#Zad. 1
numbers = [i for i in range(31)]
for n in numbers:
    numbers[n] *= 2
file = open("numbers.txt", "w")
file.writelines(str(numbers))
file.close()

#Zad. 2
file = open("numbers.txt", "r")
print(file.readlines())
file.close()

#Zad. 3
with open("newtext.txt", "w") as file:
    file.writelines(["Roses are red\n", "Violets are blue\n", "Goats and sheep smell\n", "And so do you\n"])

with open("newtext.txt", "r") as file:
    print(file.read())

#Zad. 4
class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print("Nazwa produktu: {}".format(self.nazwa_produktu))
        print("Ilosc: {}".format(self.ilosc))
        print("Jednostka miary: {}".format(self.jednostka_miary))
        print("Cena jednostkowa: {}".format(self.cena_jed))

    def ile_produktu(self):
        print("{} {}".format(self.ilosc, self.jednostka_miary))

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

ser = NaZakupy("ser", 0.3, "kg", 34.99)
ser.wyswietl_produkt()
ser.ile_produktu()
cena = ser.ile_kosztuje()
print(cena)

#Zad. 5
class CiagArytmetyczny:
    wartosci = []
    a1 = 0
    roznica = 0
    ilosc_elementow = 0

    def wyswietl_dane(self):
        print(self.wartosci)

    def pobierz_elementy(self, *elementy):
        self.wartosci.clear()
        for i in range(len(elementy)):
            self.wartosci.append(elementy[i])

    def pobierz_parametry(self, a1, roznica, ilosc_elementow):
        self.a1 = a1
        self.roznica = roznica
        self.ilosc_elementow = ilosc_elementow

    def policz_sume(self):
        suma = 0
        #for i in self.wartosci:
            # suma +=int(i)
        for i in range(len(self.wartosci)):
            suma += int(self.wartosci[i])
        return suma

    def policz_elementy(self):
        self.wartosci.clear()
        for i in range(self.ilosc_elementow):
            self.wartosci += [self.a1 + self.roznica*i]

ciag = CiagArytmetyczny()
ciag.pobierz_elementy(3, 5, 7, 9, 11, 13, 15, 17)
ciag.wyswietl_dane()
print(ciag.policz_sume())
ciag.pobierz_parametry(5, 3, 10)
ciag.policz_elementy()
ciag.wyswietl_dane()

#Zad. 6
class Robaczek:
    def __init__(self, x = 0, y = 0, krok = 1):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y += ile_krokow * self.krok

    def idz_w_dol(self, ile_krokow):
        self.y -= ile_krokow * self.krok

    def idz_w_lewo(self, ile_krokow):
        self.x -= ile_krokow * self.krok

    def idz_w_prawo(self, ile_krokow):
        self.x += ile_krokow * self.krok

    def pokaz_gdzie_jestes(self):
        print("{}, {}".format(self.x, self.y))
=======
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

>>>>>>> origin/master
