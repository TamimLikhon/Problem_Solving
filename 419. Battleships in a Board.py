board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]

n = len(board)

calc = []

for i in range(n):
    calc.append(board[i].count("X"))
    

print(max(calc))