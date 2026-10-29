class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m,n=len(grid),len(grid[0])
        visited=set()
        dirs=[[0,1],[1,0],[-1,0],[0,-1]]
        res=0
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]=='0':
                return
            for dr,dc in dirs:
                r,c=i+dr,j+dc
                if 0<=r<m and 0<=c<n and (r,c) not in visited and grid[r][c]=='1':
                    visited.add((r,c))
                    dfs(r,c)
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j]=='1':
                    visited.add((i,j))
                    dfs(i,j)
                    res+=1
        return res