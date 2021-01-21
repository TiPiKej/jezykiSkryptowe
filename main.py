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

pattern1 = re.compile('Niebieski')
result_1 = pattern1.finditer(bridge_of_death)

iter_arr = [[substring.span()[0], substring.span()[1]] for substring in result_1]

print(bridge_of_death.)
print("1 element: {} na pozycji {} {}".format(iter_arr[0], iter_arr[0][0], iter_arr[0][1]))
print("Ostatni element: {} na pozycji {} {}".format(iter_arr[-1], iter_arr[-1][0], iter_arr[-1][1]))
