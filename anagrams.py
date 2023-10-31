# Tehtäväsi on muodostaa lista, jossa on kaikki 
# annetun merkkijonon anagrammit eli kaikki merkkijonot, 
# jotka voidaan muodostaa merkkijonon merkeistä. 
# Listan tulee olla aakkosjärjestyksessä.


def create(sana):

    if len(sana) <= 1:
        return [sana]
    else:
        taulukko = []
        for c in create(sana[1:]):
            for i in range(len(sana)):
                taulukko.append(c[:i] + sana[0:1] + c[i:])
        # Aakkosjärjestykseen ja poistetaan duplikaatit     
        return list(dict.fromkeys(sorted(taulukko)))

        
if __name__ == "__main__":
     print(create("a"))
     print(create("ab")) # [ab,ba]
     print(create("abac")) # [aabc,aacb,abac,abca,acab,acba,baac,baca,bcaa,caab,caba,cbaa]
     print(len(create("aybabtu"))) # 1260