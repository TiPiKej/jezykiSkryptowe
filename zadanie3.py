liczba_prob = 5
klucz = "slowo"

for i in range(liczba_prob):
    in_klucz = input()
    if klucz == in_klucz:
        print("Gratulacje, odgadłeś słowo!")
        break
else:
    print("Przegrałeś")
