import re

bridge_of_death = '''
-Jaki jest twój ulubiony kolor?
-Niebieski!
-Dobrze. Idź.
...
-Stój. Jakie jest twe imię?
-Sir Galahad z Camelotu.
-Jaki jest twój cel?
-Odnaleźć Graala.
-Jaki jest twój ulubiony kolor?
-Niebieski... nie... żóóóółtyyyy!
'''

print(re.findall("[a-zA-Z]{4,}", bridge_of_death))

# albo wykorzystujac metode compile
# wyrazenie = re.compile("[a-zA-Z]{4,}")
# print(wyrazenie.findall(bridge_of_death))
