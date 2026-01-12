class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cols =  [set() for _ in range(9)]
        rows =  [set() for _ in range(9)]
        boxes =  [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i//3)*3 +j//3].add(num)
        def backtrack(r,c):
            if r == 9:
                return True
            if c == 9:
                return backtrack(r + 1, 0)
            if board[r][c] != '.':
                return backtrack(r, c + 1)
            for num in '123456789':
                box_id = (r//3)*3 + c//3
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_id]:
                    board[r][c] = num
                    cols[c].add(num)
                    rows[r].add(num)
                    boxes[box_id].add(num)
                    if backtrack(r,c+1):
                        return True
                    board[r][c] ='.'
                    cols[c].remove(num)
                    rows[r].remove(num)
                    boxes[box_id].remove(num)
            return False
        backtrack(0,0)

