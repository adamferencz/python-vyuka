def load_matrix(file_path):
    """Načtení matice z textového souboru."""
    with open(file_path, 'r') as f:
        return [list(map(int, line.strip())) for line in f.readlines()]

def find_longest_horizontal_line(matrix):
    """Najít nejdelší horizontální úsečku."""
    max_length = 0
    start = end = (0, 0)
    for i, row in enumerate(matrix):
        length = 0
        for j, val in enumerate(row):
            if val == 1:
                if length == 0:
                    temp_start = (i, j)
                length += 1
                if length > max_length:
                    max_length = length
                    start = temp_start
                    end = (i, j)
            else:
                length = 0
    return start, end

def find_longest_vertical_line(matrix):
    """Najít nejdelší vertikální úsečku."""
    max_length = 0
    start = end = (0, 0)
    cols = len(matrix[0])
    for j in range(cols):
        length = 0
        for i in range(len(matrix)):
            if matrix[i][j] == 1:
                if length == 0:
                    temp_start = (i, j)
                length += 1
                if length > max_length:
                    max_length = length
                    start = temp_start
                    end = (i, j)
            else:
                length = 0
    return start, end

def find_largest_square(matrix):
    """Najít největší čtverec černých buněk."""
    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    max_size = 0
    bottom_right = (0, 0)

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                if dp[i][j] > max_size:
                    max_size = dp[i][j]
                    bottom_right = (i, j)
    
    top_left = (bottom_right[0] - max_size + 1, bottom_right[1] - max_size + 1)
    return top_left, bottom_right

# Testování s vlastní maticí
if __name__ == "__main__":
    # Načíst matici z textového souboru
    matrix = load_matrix("obrazek.txt")
    
    # Najít nejdelší horizontální úsečku
    hline_start, hline_end = find_longest_horizontal_line(matrix)
    print("Nejdelší horizontální úsečka:", hline_start, hline_end)
    
    # Najít nejdelší vertikální úsečku
    vline_start, vline_end = find_longest_vertical_line(matrix)
    print("Nejdelší vertikální úsečka:", vline_start, vline_end)
    
    # Najít největší čtverec
    square_start, square_end = find_largest_square(matrix)
    print("Největší čtverec:", square_start, square_end)
