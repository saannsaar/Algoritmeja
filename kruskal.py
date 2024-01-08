class Kruskal:
    def __init__(self, n):
        self.n = n
        self.edges = []
        
    def add_edge(self, node_a, node_b, weight):
        self.edges.append((node_a, node_b, weight))
        
    def construct(self):
        self.edges.sort(key=lambda x: x[2])

        uf = UnionFind(self.n)
        edges_count = 0
        tree_weight = 0

        for edge in self.edges:
            node_a, node_b, weight = edge
            if uf.find(node_a) != uf.find(node_b):
                uf.union(node_a, node_b)
                edges_count += 1
                tree_weight += weight
        
        if edges_count != self.n - 1:
            return None
        return tree_weight
    
class UnionFind:
    def __init__(self, n):
        self.link = {node: None for node in range(1, n + 1)}
        self.size = {node: 1 for node in range(1, n + 1)}
            
    def find(self, x):
        while self.link[x]:
            x = self.link[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return
 
        if self.size[a] > self.size[b]:
            a, b = b, a
        self.link[a] = b
        self.size[b] += self.size[a]        
    
if __name__ == "__main__":
    k = Kruskal()
    k.add_edge(1,2,1)
    k.add_edge(2,3,2)
    k.add_edge(3,4,3)
    k.add_edge(4,5,4)
    