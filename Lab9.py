import numpy as np
import pandas as pd

#df = pd.read_csv('autralian.txt', header=None, decimal='.')
#xlsx = pd.ExcelFile('Wyniki.xlsx')
#df = pd.read_excel(xlsx, header=0)

#Series
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
# s = pd.Series([10, 12, 8, 14], index=['a','b','c','d'])
# print(s)
# #DataFrame
# #tworzenie dataframe na podstawie słownika
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Populacja': [11190846, 1303171035, 207847528]}
# df = pd.DataFrame(data)
# print(df)
# #DataFrame przechowuje typ dla każdej kolumny co możemy sprwadzić wpisując
# print(df.dtypes)
# #możemy również w prosty sposób stworzyć serię danych -czyli próbki
# #dla kolejnych #dat, pomiarów czasu
# daty = pd.date_range('20210324', periods=5)
# print(daty)
# #df = pd.DataFrame(np.random.randn(5,4), index=daty, columns=list('ABCD'))
# print(df)
# df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa']
# print(df)

# pojedynczy element serii, odnosimy się do nazwy indeksu
print(s['c'])
# możemy również dostać się do wartości serii jak do pola klasy
print(s.c)
# pojedynczy elemenet ramki danych, tak jak przy cięciu tablic, oparte na indeksach
print(df[0:1])
print("")
# kolumna po etykiecie
print(df['Populacja'])
# pobieranie pojedynczej wartości po indeksie wiersza i kolumny
print(df.iloc[0, 0])
# pobieranie wartości po indeksie wiersza i etykiecie kolumny
print(df.loc[0, "Kraj"])
print(df.at[0, "Kraj"])
# podobnie jak wprzypadku serii można odwoływać się do kolumn jak do pól klasy
# dodatkowo print jest wywoływany jak w pętli dla każdego elementu danej kolumny
print('kraj: ' + df.Kraj)
# Pandas posiada również funkcje pozwalające na losowe pobieranie elementów lub
# w odniesieniu do procentowej wielkości całego zbioru# jeden losowy element
print(df.sample())
#n losowych elementów
print(df.sample(2))
# ilość elementów procentowo, uwaga na zaokrąglenie
print(df.sample(frac=0.5))
# jeżeli potrzeba nam więcej próbek niż znajduje się w zbiorze i dopuszczamy duplikaty
# to możemy użyć parametru replace, który będzie losował z powtórzeniami
print(df.sample(n=10, replace=True))
# zamiast wyświetlać całą kolekcje możemy wyświetlić określoną ilość elementów od początku kolekcji
# lub od jej końca
print(df.head())
print(df.head(2))
print(df.tail(1))
# Pandas jest też w stanie wyświetlić statystykę dla wartości, które dana kolekcja zawiera, o ile są jakieś kolumny
# z danymi numerycznymi
print(df.describe())
# transpozycja to zmienna T kolekcji, podobnie jak w Numpy
print(df.T)

#Zad 1
imiona_xlsx = pd.ExcelFile('imiona.xlsx')
data_frame = pd.read_excel(imiona_xlsx, header=0)

#Zad 2
print(data_frame[(data_frame.Liczba > 1000)])
print(data_frame[(data_frame.Imie == 'MARCIN')])
print('Suma urodzonych dzieci: ', data_frame['Liczba'].sum())
group = data_frame[(data_frame.Rok <= 2005)]
print()
