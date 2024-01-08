class Kosaraju:
    def __init__(self, n):
        self.nodes = range(1, n + 1)
        self.graph = {node: [] for node in self.nodes}
        self.reverse = {node: [] for node in self.nodes}
        
    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.reverse[b].append(a)
        
    def visit(self, node, phase):
        if node in self.visited:
            return
        self.visited.add(node)

        if phase == 1:
            graph = self.graph
        if phase == 2:
            graph = self.reverse
        
        for next_node in graph[node]:
            self.visit(next_node, phase)

        if phase == 1:
            self.order.append(node)
        
    def count_components(self):
        self.visited = set()
        self.order = []
        
        for node in self.nodes:
            self.visit(node, 1)
                
        self.order.reverse()
        self.visited.clear()

        count = 0
        for node in self.order:
            if node not in self.visited:
                count += 1
                self.visit(node, 2)
                
        return count

if __name__ == "__main__":
        k = Kosaraju(100)
        n = 100
        for a in range(1,n): 
            for b in range(a+1, n+1):
                k.add_edge(a, b)
        print(k.graph)
        print(k.count_components())
       
    

 