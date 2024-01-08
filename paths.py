def create(x):
    if x <= 0 or x > 10**9:
        raise ValueError("Invalid value for x")

    edges = []

    # Create a tree-like structure with branching factor based on x
    current_node = 1
    next_node = 2

    for _ in range(x):
        # Add an edge from the current node to the next node
        edges.append((current_node, next_node))

        # Increment the next node
        next_node += 1

        # If the next node exceeds 100, reset it to 2 and move to the next level
        if next_node > 100:
            next_node = 2
            current_node += 1

    # Add an edge from the last node to 100
    edges.append((current_node, 100))

    return edges

if __name__ == "__main__":
    print(create(2))  # Example: [(1, 2), (1, 100), (2, 100)]
    print(create(5))
    print(create(10))
    # print(create(123456789))
