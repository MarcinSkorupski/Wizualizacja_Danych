import numpy as np

#inicjujemy dane
a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(a)
print(b)
#wykonujemy operację i zapisujemy do nowej zmiennej
c = a -b
print(c)
#wykonujemy operację: kwadrat zawartości
print(b**2)
#możemy również zmodyfikować obecne zmienne
print(a)
a += b
print(a)
a -= b
print(a)

a = np.arange(12).reshape((3,4))
print(a)
#suma całej macierzy
print(a.sum())
#suma każdej z kolumn
print(a.sum(axis=0))
#minimum każdego rzędu
print(a.min(axis=1))
#skummulowana suma dla rzędu
print(a.cumsum(axis=1))

#inicjujemy dane
a = np.array([[2, 1, 3], [-1, 2, 4]])
b = np.array([[1, 3], [2, -2], [-1, 4]])
c = np.dot(a,b)
#mnożenie macierzy
print(c)
d = a.dot(b)
print(d)

b = np.arange(3)
print(b)
print(np.exp(b))
print(np.sqrt(b))
c = np.array([2., -1., 4.])
print(np.divide(b,c))

#generujemy macierz 3x2
a = np.arange(6).reshape((3,2))
print(a)
for b in a.flat:
#iterujemy wzdłuż pierwszej osi
    print(b)
    print("")

#generujemy macierz 1x6
a = np.arange(6)
print(a)
print(a.shape)
#generujemy macierz 3x3
b = np.array([np.arange(3), np.arange(3), np.arange(3)])
print(b)
print(b.shape)
print("")


#Zad 1
a1 = np.array([3.4, 7, -0.3])
b1 = np.array([-12, 1.1, 4.8])
c1 = np.multiply(a1, b1)
print(c1)
print("")

#Zad 2
a2 = np.array([a1, c1, b1])
b2 = np.array([i + (-1)**i for i in range(16)])
b2 = b2.reshape(4, 4)
min_col_a = np.min(a2, axis=0)
min_row_a = np.min(a2, axis=1)
min_col_b = np.min(b2, axis=0)
min_row_b = np.min(b2, axis=1)
print(min_col_a)
print(min_row_a)
print(min_col_b)
print(min_row_b)
print("")

#Zad 3
a3 = a1.dot(b1)
print(a3)
print("")

#Zad 4
a4 = np.array([6, -4, 11])
b4 = np.array([3.45, 2., 6.79])
c4 = np.multiply(a4, b4)
print(c4)
print("")

#Zad 5
a5 = np.array([a4, b4])
a = np.sin(a5)
print(a)
print("")

#Zad 6
a6 = np.array([c4, min_row_a])
b = np.cos(a6)
print(b)
print("")

#Zad 7
c7 = np.add(a, b)
print(c7)
print("")

#Zad 8
a8 = np.arange(9).reshape(3, 3)
for row in a8:
    print(row)
print("")

#Zad 9
a9 = np.array([[4, -1.4, 9], [-3.3, 0, 123], [5, 9.43, -4]])
for i in a9.flat:
    print(i)
print("")

#Zad 10
a10 = np.array([3.2 * i - 2.8 for i in range(81)]).reshape(9, 9)
b10 = a10.reshape(3, 27)
c10 = a10.reshape(27, 3)
d10 = a10.reshape(81, 1)
print(a10)
#print(b10)
#print(c10)
#print(d10)
print("")

#Zad 11
a11 = np.arange(12)
b11 = a11.reshape(3, 4).flatten()
c11 = a11.reshape(4, 3).flatten()
d11 = a11.reshape(2, 6).flatten()
print(b11)
print(c11)
print(d11)