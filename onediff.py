# Tehtäväsi on etsiä listasta pisin alijono, 
# jossa jokaisen kahden vierekkäisen luvun ero on enintään 1
# Esimerkiksi listassa [5,2,3,8,2,4,1]
# pisin tällainen alijono on [2,3,2,1]
# jonka pituus on 4
# Voit olettaa, että 1≤n≤100
# ja jokainen listan alkio on kokonaisluku välillä 1≤n≤100

def pisinAlijonoYhdenerolla(arr, n):
    
    apuarr = [1 for i in range(n)]
   
    # Looptaan annettu taulukko
    for i in range(n):
        # Verrataan kaikkiin edellisiin 
        for j in range(i):
            
            if ((arr[i] == arr[j]+1) or (arr[i] == arr[j]-1) or (arr[i] == arr[j])):
               
                apuarr[i] = max(apuarr[i], apuarr[j]+1)
 
    # Etsitään isoin luku aputaulukosta 
    result = max(apuarr)
   
    return result

def find(t):
    n = len(t)
    return pisinAlijonoYhdenerolla(t, n)

if __name__ == "__main__":
    print(find([1,2,3,4,5])) # 5
    print(find([5,5,5,5,5])) # 5
    print(find([5,2,3,8,2,4,1])) # 4
    print(find([1,3,5,7,9])) # 1