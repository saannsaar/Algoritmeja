# Tehtäväsi on muodostaa lista, jossa on kaikki n
# merkin pituiset merkkijonot, joissa jokainen merkki 
# on A, B tai C ja missään kohdassa ei ole vierekkäin kahta 
# samaa merkkiä. Listan tulee olla aakkosjärjestyksessä.


def search(result, s, n):
    # taulukko jossa on kirjaimet mitä käytetään stringien muodostamisessa
    kirjaimet = ["A", "B", "C"]
    if len(s) == n:
        result.append(s)
    else:
        if(len(s) > 0):
            # viimeisen kirjaimen pythonilla saa string[-1] eli esim
            # stringi = "Moikku"
            # stringi[-1] olisi "u"
            # tsekataan vika kirjain mikä "s" stringissä on
            #  jotta voidaan poistaa se kirjaimet listasta
            # jotta sitä ei lisätä perään koska se on jo muodostetussa "s" stringissä
            viimenenkirjain = s[-1]
            kirjaimet.remove(viimenenkirjain)
            # Käydään kirjaimet taulukko läpi ja lisätään "s" stringiin
            # kirjaimet taulukosta kirjain (ja koska on poistettu äsken ne
            # mitä oli jo stringissä voidaan lisätä vain uniikkeja)
            for kirjain in kirjaimet:
                search(result, s+kirjain, n)
        else:   
                # Tällä saadaan lisättyä aina ensimmäinen kirjain s stringiin
                search(result, s+"A", n)
                search(result, s+"B", n)
                search(result, s+"C", n)

def create(n):
    result = []
    s = ""
    search(result, "", n)
    return result
        
if __name__ == "__main__":
    print(create(1)) # [A,B,C]
    print(create(2)) # [AA,AB,AC,BA,BB,BC,CA,CB,CC]
    print(create(3))
    print(len(create(5))) # 243