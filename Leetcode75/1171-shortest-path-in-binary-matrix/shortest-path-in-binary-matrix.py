class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        dirs=[(0,-1),(0,1),(1,0),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        q=deque([(0,0,1)])
        grid[0][0]=1
        while q:
            i,j,d=q.popleft()
            if i==n-1 and j==n-1:
                return d
            for dr,dc in dirs:
                di,dj=dr+i,dc+j
                if 0<=di<n and 0<=dj<n and grid[di][dj]==0:
                    grid[di][dj]=1
                    q.append((di,dj,d+1))
        return -1
