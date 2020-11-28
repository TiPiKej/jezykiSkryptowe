try:
    zawartosc = ""
    with open("plik.txt", "r") as file:
        for line in file:
            zawartosc += line
    with open("plik2.txt", "w") as file:
        file.write(zawartosc)
except IOError as ioe:
    print(ioe)
