from random import randint

imiona = ['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa']

pierwsze_litery = [imie[0] for imie in imiona]
losowe_liczby = [[randint(1, 10) for j in range(4)] for i in range(5)]

print(imiona)
print(pierwsze_litery)
print(losowe_liczby)
