file = open("plik.txt", "w+")

for i in range(10):
    for j in range(10):
        file.write(str(i*j) + " ")
    file.write("\n")

file.seek(0)

for line in file:
    print(line, end="")

file.close()
