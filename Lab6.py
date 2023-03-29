#Zestaw A
#Zad. 1
print("Podaj dwie liczby calkowite: ")
a = input()
b = input()
try:
    a = int(a)
    b = int(b)
    c = a*a + a * b + b*b
    with open("zadanie1.txt", 'w') as file1:
        file1.write(str(c))
except ValueError:
    print("Przynajmniej jedna z podanych wartosci nie byla liczba calkowita")

#Zad. 2
def sum_of_lists(a, b):
    sum = []
    for i in range(len(a)):
        sum.append(a[i] + b[i])
    return sum

list1 = [i + 3 for i in range(10)]
list2 = [3 * i for i in range(10)]
list3 = sum_of_lists(list1, list2)
print(list3)

#Zad. 3
file3 = open("tekst.txt", 'r', encoding='utf-8')
file3.seek(100)
znaki = file3.read(35)
file3.close()
ilosc = 0
for znak in znaki:
    if (znak.isupper()):
        print(znak)
        ilosc += 1
if (ilosc == 0):
    print("Nie ma wielkich liter.\n")
else:
    print(ilosc)

#Zad. 4
numbers = [4 * i + 2 for i in range(10)]
threshold = 13
numbers_over_threshold = [number for number in numbers if number > threshold]

print(numbers_over_threshold)

#Zad. 5
import math
result = math.pow(math.pow(math.e, 3) + math.cos(39)**2, 1/5) + math.pow(2/7, 3) + math.pi
print(round(result, 2))


#Zestaw B
#Zad. 1
file1 = open("tekst.txt", 'r', encoding='utf-8')
file1.seek(71)
znaki = file1.read(40)
file1.close()
ilosc = znaki.count('A')
if (ilosc == 0):
    print("Wielka litera A nie wystepuje.")
else:
    print(ilosc)

#Zad. 2
numbers = [5, 3.7, -9.999, 15, -23, 2.]
floats = [number for number in numbers if type(number) == float]
print(floats)

#Zad. 3
def add_sums(list):
    sums = [list[0] + number for number in list]
    list.extend(sums)
    return list

print(add_sums(numbers))

#Zad. 4
result = math.sin(56)**2 + math.pow((4**2/25) + math.log(85, 3), 1/4)
print(round(result, 2))