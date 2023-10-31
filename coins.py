# Sinulla on n kolikkoa ja jokaisella kolikolla on
# jokin kokonaislukuarvo. Tehtäväsi on laskea, 
# montako eri summaa voit muodostaa käyttämällä kolikoita.

# Esimerkiksi kun kolikot ovat [3,4,5] , mahdolliset summat ovat 3
#, 4, 5, 7, 8, 9 ja 12. Tässä tapauksessa on siis 7
# mahdollista summaa. Huomaa, että summassa tulee olla vähintään yksi kolikko eli tyhjä ratkaisu ei kelpaa.
# Voit olettaa, että 1≤n≤100 ja jokaisen kolikon arvo on välillä 1…100

from collections import Counter

def count(t):
    maxsumma= sum(t)
    counter = Counter()

    for item in t:

        for atm_num in range(maxsumma, -1, -1):
            if atm_num == 0 or atm_num in counter:
                counter[atm_num + item] += 1

    return len(counter)


if __name__ == "__main__":
    print(count([3,4,5])) # 7
    print(count([1,1,2])) # 4
    print(count([2,2,2,3,3,3])) # 13
    print(count([42,5,5,100,1,3,3,7])) # 91
    print(count([82, 81, 51, 52, 87, 9, 85, 46, 75, 87, 33, 75, 65, 42, 64, 82, 3, 98, 38, 20, 88, 21, 68, 59, 12, 73, 63, 49, 71, 17, 28, 97, 25, 22, 16, 83, 60, 61, 28, 82, 48, 92, 44, 87, 83, 71, 91, 54, 43, 66, 49, 49, 12]))