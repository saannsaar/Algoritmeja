#Verkossa on n
#solmua ja se on aluksi tyhjä. 
#Tehtäväsi on toteuttaa luokka, 
#jonka avulla pystyy lisäämään kaaren verkkoon 
#sekä tutkimaan, voiko solmut värittää kahdella 
#värillä niin, että jokainen kaari 
#yhdistää kaksi eriväristä solmua.

class Coloring:
    def __init__(self,n):
        self.verkko = [[] for _ in range(n+1)]

    def add_edge(self,a,b):
         self.verkko[a].append(b)
         self.verkko[b].append(a)

    def check(self):
        n = len(self.verkko) # solmujen määrä
        varilista = [0]*n  
        for solmu in range(n): # käydään kaikki solmut läpi
            if varilista[solmu] == 0:
                if coloring(solmu, 'musta', varilista, self.verkko) == False:
                    return False
        return True
    

#funktio jossa kokeillaan saadaanko väritettyä 
def coloring(solmu, vari, varilista, verkko):
    varilista[solmu] = vari
    print(verkko)
    print(varilista)
    for i in verkko[solmu]:
        # Viereisellä on sama väri 
        print("--", varilista[i], i)
        if varilista[i] == vari:
            return False
        elif varilista[i] == 0 and coloring(i, opp(vari), varilista, verkko) == False:
            return False
    return True


# palauttaa päinvastasen värin
def opp(vari):
    if vari =='musta':
        return 'valkoinen'
    elif vari =='valkoinen':
        return 'musta'

if __name__ == "__main__":
    c = Coloring(4)
    c.add_edge(1,2)
    c.add_edge(2,3)
    c.add_edge(3,4)
    c.add_edge(1,4)
    print(c.check()) # True
    c.add_edge(2,4)
    print(c.check()) # False



