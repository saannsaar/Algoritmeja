def countSteps(n, lista):
     
    # Talllennetaan counteriin mahdollisten hyppytapojen määrä
    counter = [0] * (n + 1)
    counter[0] = 1
    print(counter)

     
    # luupataan portaiden läpi
    for i in range(1, n+1):
        
        numberof_ways = 0
         
        for j in lista:
             
            
            if (i - j >= 0):

                numberof_ways += counter[i - j]
                
            counter[i] = numberof_ways
            print(counter)
 
    return counter[n]
	

def count(n,a,b):
       lista = []
       lista.append(a)
       lista. append(b)
     
   
       return countSteps(n,lista)

if __name__ == "__main__":
    print(count(4,1,2)) # 5
    print(count(10,2,5)) # 2
    print(count(10,6,7)) # 0
    print(count(30,3,5)) # 58
    print(count(50,2,3)) # 525456