def sort_(list_to_sort):
    for i in range(len(list_to_sort)):
        min = i
        for j in range(i, len(list_to_sort)):
            if list_to_sort[min][1] > list_to_sort[j][1]:
                min = j
            elif list_to_sort[min][1] == list_to_sort[j][1] and list_to_sort[min][2] > list_to_sort[j][2]:
                min = j
        list_to_sort[i], list_to_sort[min] = list_to_sort[min], list_to_sort[i]
    return list_to_sort


list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
list_to_sort_2 = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]

sort_(list_to_sort)
sort_(list_to_sort_2)

print(list_to_sort)
print(list_to_sort_2)
