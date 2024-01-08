class CountPaths:
    def __init__(self, n):
        self.nodes = range(1, n + 1)
        self.graph = {node: [] for node in self.nodes}
        
    def add_edge(self, a, b):
        self.graph[a].append(b)
        
    def count_from(self, node):
        if node in self.result:
            return self.result[node]
        
        path_count = 0
        for next_node in self.graph[node]:
            path_count += self.count_from(next_node)
        
        self.result[node] = path_count
        return path_count
        
    def count_paths(self, x, y):
        self.result = {y: 1}
        return self.count_from(x)
    
if __name__ == "__main__":
        k = CountPaths(100)
        n = 100
        for a in range(1,n): 
            for b in range(a+1, n+1):
                k.add_edge(a, b)
        print(k.graph)
        print(k.count_paths())
       