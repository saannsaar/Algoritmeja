
# Dynaamisen ohjelmoinnin ratkaisu tässäkin
def count(t):
        tPituus = len(t)
        # Pitää määrittää laske aputaulukon koko annetun taulukon t suurimman arvon mukaan (+1)
        laske = [0] * (max(t) + 1)
        for i in range(tPituus):
                # Ylhäältä alaspäin
                for j in range(t[i] - 1, -1, -1):
                    # Päivitetään laske-taulukkoa lisäämällä arvo laske[j] arvoon laske[t[i]]
                    # Tässä siis on alijonojen määrä jotka päätyy t[i]:hin
                    laske[t[i]] += laske[j]
                # +1 koska t[i] voi muodostaa myö oman nousevan alijonon
                laske[t[i]] += 1

        result = sum(laske)
        return result

if __name__ == "__main__":
    print(count([1, 1, 2, 2, 3, 3])) # 26
    print(count([1, 1, 1, 1])) # 4
    print(count([5, 4, 3, 2, 1])) # 5
    print(count([4, 1, 5, 6, 3, 4, 1, 8])) # 37
    print(count([9, 6, 10, 10, 300, 6, 7, 6, 5, 7])) #28
    print(count([9, 6, 10, 10, 3, 6, 7, 6, 5, 7])) # 29