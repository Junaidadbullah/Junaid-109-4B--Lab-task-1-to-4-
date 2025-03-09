def Safe(board, r, c, n):
    for i in range(c):
        if board[r][i] == 1:
            return False
    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(r, n, 1), range(c, -1, -1)):
        if board[i][j] == 1:
            return False
    return True  

def solveQ(board, c, n):
    if c == n:  
        return True
    for r in range(n):
        if Safe(board, r, c, n):
            board[r][c] = 1  
            if solveQ(board, c + 1, n): 
                return True
            board[r][c] = 0  
    return False 

def nQueens(n):
    board = [[0] * n for _ in range(n)]
    if solveQ(board, 0, n):
        print(f"Max {n} queens on a {n}x{n} board can be placed.")
        for r in board:
            for i in r:
                if i == 1:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
    else:
        print("No solution.")

n = int(input("Enter board size: "))
nQueens(n)