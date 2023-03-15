#Zad.1
import math

print(math.e**10)
print(pow(math.log(5+math.sin(8)**2), 1/6))
print(3.55)
print("{0:0.2f}\n".format(4.8))

#Zad.2
imie = "MARCIN"
nazwisko = "SKORUPSKI"
print("{} {}\n".format(imie.capitalize(), nazwisko.capitalize()))

#Zad.3
lyrics = "Dark master within, I will fight for you. Dark master of sin, now my soul is yours. Dark master, my guide, I will die for you. Dark master inside."
master_count = lyrics.count("master")
print(master_count)
print('')

#Zad.4
text = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
print(text[1])
print(text[len(text)-1])
print('')

#Zad.5
split_text = text.split()
print(split_text)
print('')

#Zad.6
float = 4.945436
hexadec = 0x4d7f
print(imie)
print("{0:0.2f}".format(float))
print("{:02X}\n".format(hexadec))

#Zad.7
sports = ["tennis", "volleyball", "golf"]
sports.reverse()
sports.extend(["football", "basketball"])
print(sports)
print('')

#Zad.8
abbreviations = {'itp': 'i tym podobne', 'btw': 'by the way', 'imho': 'in my honest opinion'}
print(abbreviations)
print('')

#Zad.9
games = {'Battle brothers': 'tactic/strategy', 'The Witcher 3': 'rpg', 'Team fortress 2': 'fps', 'Rome: Total War': 'grand strategy'}
games_count = len(games)
print(games)
print(games_count)
print('')

#Zad.10
sentence = input('Napisz zdanie: ')
a_count = sentence.count('a')
A_count = sentence.count('A')
print(a_count + A_count)
print('')

#Zad.11
a = input("Podaj liczbe calkowita a:")
b = input("Podaj liczbe calkowita b:")
c = input("Podaj liczbe calkowita c:")
max = max(a, b, c)

if (a == max):
    print("Liczba a jest najwieksza.\n")
if (b == max):
    print("Liczba b jest najwieksza.\n")
if (c == max):
    print("Liczba c jest najwieksza.\n")

#Zad.12
numbers = [4, 6.7, 2, -7, -8.33, 0.01]
for i in numbers:
    #numbers[i] = pow(numbers[i], 2)

print(numbers)
print('')
