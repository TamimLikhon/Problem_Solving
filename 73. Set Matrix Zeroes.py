matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

rows, cols = len(matrix), len(matrix[0])
new_mat = [[0]*cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            new_mat[i] = [0] * cols  # Set entire row to 0
            for k in range(rows):
                new_mat[k][j] = 0  # Set entire column to 0

print(new_mat)
