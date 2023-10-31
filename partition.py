# Annettuna on lista kokonaislukuja ja 
# tehtäväsi on selvittää, onko luvut mahdollista 
# jakaa kahteen ryhmään niin, että molempien ryhmien summa on sama.

#Esimerkiksi kun lista on [9,4,8,7,6]
#, mahdollinen ratkaisu on muodostaa ryhmät [8,9]
# ja [4,6,7]
#. Tällöin kummankin ryhmän lukujen summa on 17


def onkoSamatSummat(arr, leng, summa):
    if summa == 0:
        return True
    if leng == 0 and summa != 0:
        return False
 
   
    if arr[leng-1] > summa:
        return onkoSamatSummat(arr, leng-1, summa)

    return onkoSamatSummat(arr, leng-1, summa) or onkoSamatSummat(arr, leng-1, summa-arr[leng-1])
 


def check(t):
    #Lasketaan taulukon summa
    summa = 0
    n = len(t)
    for i in range(0, n):
        summa += t[i]
    # Jos summa ei ole parillinen luku, ei voi olla kahta listaa
    # joilla olisi sama summa eli ei kutsuta edes toista funktiota turhaan
    if summa % 2 != 0:
        return False
 
    return onkoSamatSummat(t, n, summa // 2)
 
 


if __name__ == "__main__":
    print(check([3,4,5])) # False
    print(check([16,8,4,4])) # True
    print(check([9,4,8,7,6])) # True
    print(check([1,2,3,4,5,6])) # False
    print(check([1,2,3,4,5,6,7])) # True
    print(check([4,4,4,6,6])) # True