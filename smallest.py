import random
import time
import heapq

# Järjestää listan ja laskee n/10 pienimmän alkion summan
def algoritmi1(lista):
   
    jarjestetty = sorted(lista)
    jako = len(jarjestetty)//10
    summa = sum(jarjestetty[:jako])
    return summa

def algoritmi2(lista):
    keko = []
    for num in lista:
        heapq.heappush(keko, num)
        # Tarkistetaan onko keon koko > alkuperäisen listan pituus / 10 
        if len(keko) > len(lista)//10:
            heapq.heappop(keko)
    summa = sum(keko)
    return summa

def generoiLista(n):
    return [random.randint(1, 10**9) for _ in range(n)]

def testi():
    n = 10**6
    d = 100
    lista = generoiLista(n)

    alku = time.time()
    result_1 = algoritmi1(lista)
    loppu = time.time()

    print(f"Algoritmi 1: {result_1}")
    print(f"Algoritmi 1 aika: {loppu - alku} sekuntia")

    alku2 = time.time()
    result_2 = algoritmi2(lista)
    loppu2 = time.time()
    print(f"Algoritmi 2: {result_2}")
    print(f"Algorithm 2 aika: {loppu2 - alku2} sekuntia")

if __name__ == "__main__":
    testi()
