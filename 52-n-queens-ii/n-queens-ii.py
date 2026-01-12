class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        board =[['.' for _ in range(n)] for _ in range(n)]

        col = [False]*n
        diag1 = [False]*(2*n -1)
        
        diag2 = [False]*(2*n -1)

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for c in range(n):
                if col[c] or diag1[row - c + n - 1] or diag2[row + c]:
                    continue
                board[row][c] ='Q'
                col[c] = diag1[row - c + n - 1] = diag2[row + c] = True
                backtrack(row + 1)


                board[row][c] ='.'
                col[c] = diag1[row - c + n - 1] = diag2[row + c] = False
        backtrack(0)
        return len(res)


        

        