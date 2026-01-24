from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = float('inf')
        
        # distance matrix
        dist = [[INF] * (n + 1) for _ in range(n + 1)]
        
        # distance to itself is 0
        for i in range(1, n + 1):
            dist[i][i] = 0
        
        # fill given edges
        for u, v, w in times:
            dist[u][v] = min(dist[u][v], w)
        
        # Floyd–Warshall
        for via in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if dist[i][via] + dist[via][j] < dist[i][j]:
                        dist[i][j] = dist[i][via] + dist[via][j]
        
        ans = max(dist[k][1:])
        return ans if ans < INF else -1
