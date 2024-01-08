#Annettuna on lista, jossa on n kokonaislukua. Tehtäväsi on luoda uusi lista, jossa on kaikki tämän listan osajoukkojen summat pienimmästä suurimpaan.
#Voit olettaa, että 1 \le n \le 10. Algoritmisi tulee toimia tehokkaasti kaikissa näissä tapauksissa.

def create(t):

    summa = [0]
    for i in range(len(t)):
        for x in range(len(summa)):
            summa.append(summa[x] + t[i])

    summa.sort()
    return summa


if __name__ == "__main__":
    print(create([1, 2, 3])) # [0, 1, 2, 3, 3, 4, 5, 6]
    print(create([42, 1337])) # [0, 42, 1337, 1379]
    print(create([1, 1, 1])) # [0, 1, 1, 1, 2, 2, 2, 3]
    print(create([5])) # [0, 5]