class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class TreeSet:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            self.size += 1
            return

        node = self.root
        while True:
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    self.size += 1
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    self.size += 1
                    return
                node = node.right

    def __contains__(self, value):
        if not self.root:
            return False

        node = self.root
        while node:
            if node.value == value:
                return True
            if node.value > value:
                node = node.left
            else:
                node = node.right

        return False
    
    def __repr__(self):
        items = []
        self.traverse(self.root, items)
        return str(items)

    def traverse(self, node, items):
        if not node:
            return
        self.traverse(node.left, items)
        items.append(node.value)
        self.traverse(node.right, items)

    def __len__(self):
        return self.size
    
    def height(self):
        return self.calculateHeight(self.root)
    

    def calculateHeight(self, node):
        if not node:
            return -1
        leftHeight = self.calculateHeight(node.left)
        rightHeight = self.calculateHeight(node.right)
        return max(leftHeight, rightHeight) + 1
    
    def min(self):
        return self.etsiPienin(self.root).value if self.root else None

    def etsiPienin(self, node):
        while node.left:
            node = node.left
        return node

    def max(self):
        return self.etsiIsoin(self.root).value if self.root else None

    def etsiIsoin(self, node):
        while node.right:
            node = node.right
        return node

    def prev(self, x):
        return self.etsiEdellinen(self.root, x)

    def etsiEdellinen(self, node, x):
        prevNode = None
        while node:
            if node.value >= x:
                node = node.left
            else:
                prevNode = node
                node = node.right
        return prevNode.value if prevNode else None

    def next(self, x):
        return self.etsiSeuraava(self.root, x)

    def etsiSeuraava(self, node, x):
        nextNode = None
        while node:
            if node.value <= x:
                node = node.right
            else:
                nextNode = node
                node = node.left
        return nextNode.value if nextNode else None
if __name__ == "__main__":
    s = TreeSet()
    s.add(2)
    s.add(5)
    print(s.prev(5)) # 2
    print(s.prev(2)) # None
    print(s.next(1)) # 2
    print(s.next(2)) # 5
    print(s.next(5)) # None