

from time import perf_counter
def f(n):
    if (n <= 2):
        return n
    return f(n-1)+f(n-2)+f(n-3)
  
starttime = perf_counter()
f(30)
endtime = perf_counter()


print(f"Suoritusaika = {endtime-starttime} sekunttia ja tulos ={f(30)}")