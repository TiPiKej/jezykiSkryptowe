liczba_prob = 5
sukces = False
klucz = "slowo"

for i in range(liczba_prob):
    in_klucz = input()
    if klucz == in_klucz:
        sukces = True
        break

print("Gratulacje!" if sukces else "Przegrales!")
