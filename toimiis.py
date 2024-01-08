

class MaximumFlow:
    def __init__(self,n):
        self.nodes = range(1, n + 1)
        self.graph = {}
        for i in self.nodes:
            for j in self.nodes:
                self.graph[(i, j)] = 0

    def add_edge(self, node_a, node_b, capacity):
        self.graph[(node_a, node_b)] += capacity

    def add_flow(self, node, sink, flow):
        if node in self.seen:
            return 0
        self.seen.add(node)
        if node == sink:
            return flow
        for next_node in self.nodes:
            if self.flow[(node, next_node)] > 0:
                new_flow = min(flow, self.flow[(node, next_node)])
                inc = self.add_flow(next_node, sink, new_flow)
                if inc > 0:
                    self.flow[(node, next_node)] -= inc
                    self.flow[(next_node, node)] += inc
                    return inc
        return 0

    def construct(self, source, sink):
        self.flow = self.graph.copy()
        total = 0
        while True:
            self.seen = set()
            add = self.add_flow(source, sink, float("inf"))
            if add == 0:
                break
            total += add
        return total
    
if __name__ == "__main__":
    d = MaximumFlow(5)
    print(d.construct(1, 5))  # Output: 0
    d.add_edge(1, 2, 1)
    d.add_edge(2, 5, 1)
    print(d.construct(1,5))  # Output: 1
    d.add_edge(1, 5, 1)
    print(d.construct(1,5))  # Output: 2
