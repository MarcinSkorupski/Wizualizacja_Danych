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