import sys

def count(x):
    print("X =", x)
    if(x % 5 == 0):
        return x // 5
    
    vitosenKolikoilla = x % 5
    print("JAKOJÄÄNNÖS 5=",vitosenKolikoilla)
    kakkosenKolikoilla = vitosenKolikoilla % 2
    print("JAKOJÄÄNNÖS 2=",kakkosenKolikoilla)
    if(kakkosenKolikoilla == 0):
        print("TÄSTÄ",x)
        return ((x - vitosenKolikoilla) // 5 )+ (vitosenKolikoilla // 2)
    else:
       return ((x - vitosenKolikoilla) // 5 )+ ((vitosenKolikoilla - kakkosenKolikoilla) // 2) + kakkosenKolikoilla
if __name__ == "__main__":
    print(count(13)) # 3
    print(count(15)) # 3
    print(count(4)) # 2
    print(count(12345)) # 2469
    print(count(1337**9)) # 2730314408854633746890878156