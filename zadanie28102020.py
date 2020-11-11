def klucz(e):
    return e[1], e[2]


list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
list_to_sort.sort(key=klucz)
print(list_to_sort)
