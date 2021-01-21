import re


pattern_func = re.compile(r'''
\A
\ *  # Dowolna liczba spacji.
(def)  # Grupa nr 1.
\   # Spacja.
(  # Grupa nr 2 - nazwa funkcji i parametry.
([a-z_][a-z_0-9]*)  # Grupa nr 3 - nazwa funkcji.
\(((?:\*{0,2}[a-z_][a-z_A-Z0-9]*,?\*)*)  # Grupa 4- parametry.(?: oznacza grupę nieprzechwytującą.
\)
)# Grupa nr 2 - domknięcie.
(:)  # Grupa nr 5.
\Z
''', re.VERBOSE)

pattern_var = re.compile(r'\A\ *([a-z_][a-z_0-9]*)\Z', re.VERBOSE)

name = input("Wpisz nazwe zmiennej lub nazwe funkcji: ")
print("{} {}moze byc uzyte jako nazwa fukcji, lub nazwa zmiennej".format(
    name,
    "" if pattern_func.match(name) or pattern_var.match(name) else "nie "
))
