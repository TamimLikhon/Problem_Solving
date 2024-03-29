mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

calc = 0

n = len(mat)  # Dimension of the square matrix

for i in range(n):
    calc += mat[i][i]  # Adding elements from the main diagonal
    calc += mat[i][n - i - 1]  # Adding elements from the anti-diagonal

# Subtract the central element if the dimension is odd
if n % 2 == 1:
    calc -= mat[n // 2][n // 2]

print(calc)
