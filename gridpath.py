def count(r):
    # Alustetaan ruudukon rivien ja sarakkeiden määrät
    rivi = len(r)
    sarake = len(r[0])

    # Alustetaan taulukko johon voidaan tallettaa min hinta jokaseen kohtaan
    hinnat = [[float('inf')] * sarake for _ in range(rivi)]

    # Alustetaan vasen yläkulma
    hinnat[0][0] = r[0][0]

    # Päivitetään ensimmäinen rivi
    for j in range(1, sarake):
        hinnat[0][j] = hinnat[0][j-1] + r[0][j]
    print(hinnat)
    # Päivitetään ensimmäinen sarake
    for i in range(1, rivi):
        hinnat[i][0] = min(hinnat[i - 1][0], hinnat[i - 1][1]) + r[i][0]
    print(hinnat)
    # Täytetään loput taulukosta
    for i in range(1, rivi):
        for j in range(1, sarake):
            print("Mis ollaa ", hinnat[i-1][j], hinnat[i+1][j], "Luupissa ", hinnat[i-1][j], hinnat[i][j-1])
            hinnat[i][j] = min(hinnat[i-1][j],hinnat[i+1][j]) + r[i][j]

    # Alareunassa on min kustannus 
    print(hinnat)
    return hinnat[rivi-1][sarake-1]

if __name__ == "__main__":
    r = [[2, 1, 4, 8],
         [3, 8, 7, 2],
         [9, 5, 1, 2]]
    x = [[10, 4], 
         [5, 1], 
         [9, 9], 
         [10, 3], 
         [9, 8], 
         [2, 4], 
         [1, 9], 
         [2, 3]]
    p = [[6, 7, 6], 
         [5, 7, 4], 
         [6, 2, 7], 
         [7, 2, 9], 
         [6, 7, 7], 
         [5, 1, 6]]
    print(count(r))  # 17
    print(count(x))