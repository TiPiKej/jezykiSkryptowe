def klucz(e):
    return e[1], e[2]


list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
list_to_sort_2 = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]

list_to_sort.sort(key=klucz)
list_to_sort_2.sort(key=klucz)

print(list_to_sort)
print(list_to_sort_2)
