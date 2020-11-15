import datetime
from random import randint

long_list = [randint(0, 3000) for element in range(1000000)]

# Przeszukiwanie liniowe (bez przygotowania)
t1 = datetime.datetime.now()

for i in long_list:
    if i == -1:
        print("Znaleziono!")

t2 = datetime.datetime.now() - t1
print("Czas trwania algorytmu: ", t2)

# Przeszukiwanie liniowe z wykorzystaniem SET
t1 = datetime.datetime.now()

test_set = set(long_list)
for i in test_set:
    if i == -1:
        print("Znaleziono!")

t2 = datetime.datetime.now() - t1
print("Czas trwania algorytmu: ", t2)


#
# Wynik działania algorytmu na moim komputerze:
#
# Czas trwania algorytmu:  0:00:00.050011
# Czas trwania algorytmu:  0:00:00.019004
#
