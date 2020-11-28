def person_print(name, last_name, *others, age):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)


def test_function(pierwszy_argument, *args, first, **kwargs):
    print("pierwszy_argument: ", pierwszy_argument)
    print(args)
    print("Length: ", len(args))
    print("first: ", first)
    print(kwargs)
    print("Length: ", len(kwargs))


# test_function("jeden", "dwa", "trzy", first="jeden2", second="dwa2", third="trzy2")
person_print("imie", "nazwisko", "Krakow", "Malopolska", "Polska", age=16)

# Po przetestowaniu:
# argumenty mogą być tylko używane w kolejności:
# (argumenty, *argumenty_spakowane, argumenty_spakowane_z_kluczem, **argumenty_spakowane_z_kluczem)

# funkcje person_print sie uzyc bez zmian, lecz wywolanie musi zawierac argument z kluczem
# np.
# person_print("imie", "nazwisko", "Krakow", "Malopolska", "Polska", age=16)
