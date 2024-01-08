def find(taulukko):
        taulukonPituus = len(taulukko)
        apuarr = [[] for i in range(taulukonPituus)]

        apuarr[0].append(taulukko[0])

        for i in range(1, taulukonPituus):
            for j in range(i):
               
                if taulukko[i] > taulukko[j] and (len(apuarr[i]) < len(apuarr[j]) + 1):
                    # print("TAULUKON ALKIO", taulukko[i], "TAULUKON INDEKSI", i)
                    apuarr[i] = apuarr[j].copy()
                    # print(apuarr[i])
                    
            apuarr[i].append(taulukko[i])
        maxx = apuarr[0]
        for x in apuarr:
            if len(x) > len(maxx):
                maxx = x
        return maxx

if __name__ == "__main__":
    print(find([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find([1, 1, 1, 1])) # [1]
    print(find([5, 4, 3, 2, 1])) # [3]
    print(find([4, 1, 5, 6, 3, 4, 1, 8])) # [1, 3, 4, 8]


