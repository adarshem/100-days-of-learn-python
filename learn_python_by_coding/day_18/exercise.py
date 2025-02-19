def quadratic_space(n):
    start_value = 0
    matrix = [[0] * n for _ in range(n)]  # Creating a 2D array (n x n)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = start_value +1
            start_value += 1
    return matrix

print(quadratic_space(6))
