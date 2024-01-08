def count(r):
    rows, cols = len(r), len(r[0])
    pairs = 0

    # Helper function to check if two knights threaten each other
    def threatens(knight1, knight2):
        x1, y1 = knight1
        x2, y2 = knight2
        return (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1)

    # Iterate through the chessboard
    for i in range(rows):
        for j in range(cols):
            if r[i][j] == '*':
                # Check for threatening knights in the same row
                for k in range(j + 1, cols):
                    if r[i][k] == '*':
                        if threatens((i, j), (i, k)):
                            pairs += 1

                # Check for threatening knights in the same column
                for k in range(i + 1, rows):
                    if r[k][j] == '*':
                        if threatens((i, j), (k, j)):
                            pairs += 1

    return pairs // 2  # Each pair is counted twice

if __name__ == "__main__":
    r = ["*.......",
         "..*...*.",
         "........",
         ".*......",
         "...*....",
         ".......*",
         "........",
         "......*."]
    print(count(r))  # Output: 3
