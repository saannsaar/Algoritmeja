#Merkkijonon anagrammi sisältää kaikki 
#merkkijonon merkit jossakin järjestyksessä. 
# Tehtäväsi on muodostaa kaikki annetun merkkijonon anagrammit.




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
    print(create("abc")) # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print(create("aaaaa")) # ['aaaaa']
    print(create("abab")) # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
    print(len(create("aybabtu"))) # 1260