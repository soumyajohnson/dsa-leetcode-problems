class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        m,n=len(grid),len(grid[0])
        visited=set()
        q=deque()
        res=0
        fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        while q and fresh>0:
            for _ in range(len(q)):
                i,j=q.popleft()
                visited.add((i,j))
                for r,c in dirs:
                    dr,dc=i+r,j+c
                    if 0<=dr<m and 0<=dc<n and (dr,dc) not in visited and grid[dr][dc]==1:
                        fresh-=1
                        visited.add((dr,dc))
                        q.append((dr,dc))
            res+=1
        return res if fresh==0 else -1
