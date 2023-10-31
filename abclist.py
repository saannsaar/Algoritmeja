# Tein tämän luentovideon perusteella, en oikein keksinyt muuta ratkaisutapaa
# jos tätä ei hyväksytä niin koitan keksiä jonkin toisen tavan toteuttaa tehtävänannon

def search(result, s, n):
    if len(s) == n:
        result.append(s)
    else:
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