class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1]:
            return -1
        direction= [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

        q = deque()
        q.append((0,0,1))

        grid[0][0] = 1

        while q:
            r,c,dist = q.popleft()
            if r== n-1 and c== n-1:
                return dist
            for nr, nc in direction:
                dx = r- nr
                dy = c- nc
                if  0<= dx< n and 0<= dy< n and grid[dx][dy] == 0:
                    grid[dx][dy] = 1
                    q.append((dx,dy,dist+1))
        return -1



































        