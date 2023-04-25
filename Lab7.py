import numpy as np
#inicjalizacja tablicy
a = np.array([[0, 1], [2, 3]])
print(a)
#lub drugi sposób
a = np.arange(2, 5, 0.1)
print(a)
#wypisanie typu zmiennej talicy (nie jej elementów)
print(type(a))
#sprawdzabue typu danych tablicy
print(a.dtype)
#inicjalizacja tablicy z konkretnym typem danych
a = np.arange(2, dtype='int64')
print(a.dtype)
#zapisywanie kopii tablicy jako tablicy z innym typem
b = a.astype('float')
print(b)
print(b.dtype)
#wupisanie rozmiaru tablicy
print(b.shape)
#można też sprawdzić ilość wymiarów tablicy
print(a.ndim)
#stworzenie tablicy wielowymiarowej może wyglądać tak
#paramentrem przekazyanym do funkcji array jest obiekt
#może to być Pythonowa lista
m = np.array([np.arange(2), np.arange(2)])
print(m)
print(m.shape)
#ponownie typem jest ndarray
print(type(m))

zera = np.zeros((5,5))
jedynki = np.ones((4,4), dtype='int32')
print(zera)
print(jedynki)
#warto sprawdzic jaki jest domyslny typ danych takich tablic
print(zera.dtype)
print(jedynki.dtype)
#można również stworzyć "pustą" macierz o podanych wymiarach
#wartości umieszczane są lowowe, najpierw podawana jest
pusta = np.empty((2,2))
print(pusta)

macierz = np.array([[12, 11], [2, 1]])
print(macierz)
#do elementów tablicy możemy odwołać się tak jak do elementów listy
poz_1 = macierz[1, 1]
poz_2 = macierz[0][1]
print(poz_1)
print(poz_2)

#podobnie działa funkcja linspace, które działanie jest...
liczby_lin = np.linspace(1, 2, 5)
print(liczby_lin)
liczby_lin = np.linspace(1, 2, 5, endpoint=False)
print(liczby_lin)
#a teraz możemy utworzyć dwie macierze, najpierw wart...
z = np.indices((5, 3))
print(z)
print(z[0][1][2])
#podobnie jak w MATLAB-ie możemy tworzyć macierze diagonalne
#mat_diag = np.diag([a for a in range(5)], k=1)
#mat_diag2 = np.diag([a for a in range(5)], k=-2)
#print(mat_diag)
#print(mat_diag2)

znaki = b'ogolna'
z1 = np.frombuffer(znaki, dtype='S1')
print(z1)
z2 = np.frombuffer(znaki, dtype='S3')
print(z2)

znaki = 'ogolna'
z3 = np.array(list(znaki))
z4 = np.array(list(znaki), dtype='S1')
z5 = np.array(list(b'ogolna'))
z6 = np.fromiter(znaki, dtype='S1')
print(z3)
print(z4)
print(z5)
print(z6)

a = np.arange(10)
print(a)
s = slice(2, 7, 2)
print(a[s])
s = range(2, 7, 2)
print(a[s])
#możemy ciąć tablice również w sposób znany z cięcia list
print(a[2:7:2])
#lub tak
print(a[3:])
print(a[2:5])
print('')
#na podobny sposób pastępujemy w przypadku tablic wielowymiarowych
mat = np.arange(25)
#teraz zmieniamy kształt tablicy jednowymiarowej na macierz
mat = mat.reshape((5, 5))
print(mat)
print(mat[1:]) #od drugiego wiersza
print(mat[:, 1]) #druga kolumna jako wektor
print(mat[:, -1]) #ostatnia kolumna
print(mat[2:5, 1:3]) #2 i 3 kolumna dla 3, 4, 5 wierszy
print(mat[:, [2, 4]])#3 i 5 kolumna tak samo:
print(mat[:, range(2, 5, 2)])
print('')

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print(y)


#Zad 1
arr1 = np.arange(4, 81, 4)
print(arr1)

#Zad 2
list2_1 = [3.5, -.65, -432., 33.333, 0.1]
list2_2 = np.array(list2_1, dtype='int32') #or np.array(list2_1).astype('int32')
print(list2_2)

#Zad 3
def arraynxn(n):
    arr = np.array([2**i for i in range(n*n)])
    arr = arr.reshape((n, n))
    return arr

arr3 = arraynxn(4)
print(arr3)

#Zad 4
def arraypow(a, n):
    return 1 #np.logspace(, a**n, n)

#arr4 = arraypow(3, 7)
#print(arr4)

#Zad 5
def generate_mat_diag(vector_range):
    vec = [a for a in reversed(range(vector_range))]
    mat_diag = np.diag(vec, k=2)
    return vec, mat_diag

vec5, mat_diag5 = generate_mat_diag(7)
print(vec5)
print(mat_diag5)

#Zad 6
a6 = np.array([' ' for i in range(49)]).reshape(7, 7)
a6[2] = list(reversed('olsztyn'))
a6[5] = list('galowy')
print(a6)
