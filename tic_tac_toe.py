class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        # Rows, columns, and diagonals for each player (0: Player1, 1: Player2)
        self.rows = [[0]*n for _ in range(2)]
        self.cols = [[0]*n for _ in range(2)]
        self.diag = [0, 0]
        self.anti_diag = [0, 0]

    def move(self, row: int, col: int, player: int) -> int:
        p = player - 1  # 0-index player
        # Update counters
        self.rows[p][row] += 1
        self.cols[p][col] += 1
        if row == col: 
            self.diag[p] += 1
        if row + col == self.n - 1:
            self.anti_diag[p] += 1
        
        # Check win condition
        if (self.rows[p][row] == self.n or 
            self.cols[p][col] == self.n or 
            self.diag[p] == self.n or 
            self.anti_diag[p] == self.n):
            return player
        return 0
