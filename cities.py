# Leveyssuuntainen haku (BFS)




from collections import deque

class Cities:
    def __init__(self,n):
        self.verkko = [[] for _ in range(n+1)]

    def add_road(self,a,b):
        self.verkko[a].append(b)
        self.verkko[b].append(a)

    def has_route(self,a,b):
       
         print(a, b)
         if (a == b):
             return True
         print(self.verkko)
         if (any(a in sl for sl in self.verkko) == False or any(b in sl for sl in self.verkko) == False):
              return False
              
         
        
        # Kaikki merkataan eka False koska niissä ei ole 
        # käyty
         kayty = [False for i in range(len(self.verkko))]
         queue = deque()

         kayty[a] = True
         #Tämän hetkinen solmu merkataan käydyksi ja lisätään se jonoon
         queue.append(a)

         while (len(queue) > 0):
              a = queue.popleft()
              #Käydään läpi kaikki a:n viereiset solmut 
              # ja jos viereisessä ei olla käyty merkataan se käydyksi
              # ja lisätään se jonoon
              print(self.verkko[a])
              for i in self.verkko[a]:
                   
                   #Jos i solmu on b eli haluttu päämäärä 
                   # palautetaan True koska löydettiin reitti
                   if (i == b):
                        return True
                   #Muuten jatketaan hakua
                   if (not kayty[i]):
                        kayty[i] = True
                        queue.append(i)
        # Jos haku on käyty läpi ilman että koskaan päästiin
        # b:hen, palautetaan False
         return False



if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1,2)
    c.add_road(1,3)
    c.add_road(4,5)
    print(c.has_route(1,5)) # False
    c.add_road(3,4)
    print(c.has_route(1,5)) # True