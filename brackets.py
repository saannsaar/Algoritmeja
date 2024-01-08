def count(n, k):
    
    def helpperi(aukinaiset, suljetut, syvyys, ilmaisu):
        # Jos ollaan tultu rivin loppuun ja piirretty kaikki kaaret palautetaan 1 joka lisätään tapoja muuttujaan
        if aukinaiset + suljetut == n and syvyys == 0:
            # print(aukinaiset, suljetut)
            # print(ilmaisu)
            return 1
        tapoja = 0

        # Lisätään kaari joka aukeaa oikealle = (
        if aukinaiset < n / 2 and syvyys < k:
            # print("AUKI", aukinaiset, "SYVYYS", syvyys)
            tapoja += helpperi(aukinaiset + 1, suljetut, syvyys + 1, ilmaisu + '{')

        # Lisätään kaari joka on auki vasemmalle = )
        if suljetut < n / 2 and aukinaiset > suljetut:
            # print("SULKI", suljetut)
            tapoja += helpperi(aukinaiset, suljetut + 1, syvyys - 1, ilmaisu + '}')

        return tapoja 

    vastaus = helpperi(0, 0, 0, '')
    return vastaus




if __name__ == "__main__":
    print(count(6, 1)) # 1
    print(count(6, 2)) # 4
    print(count(6, 3)) # 5
    print(count(9, 1)) # 0
    print(count(16, 4)) # 1094
  

