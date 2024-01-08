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


if __name__ == "__main__":
    s = TreeSet()
    print(s.height()) # -1
    s.add(2)
    print(s.height()) # 0
    s.add(1)
    print(s.height()) # 1
    s.add(3)
    print(s.height()) # 1
    s.add(4)
    print(s.height()) # 2