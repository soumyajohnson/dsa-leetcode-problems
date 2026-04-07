class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        m,n=len(grid),len(grid[0])
        seen=set()
        res=0
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]=="0":
                return
            seen.add((i,j))
            for r,c in dirs:
                dr,dc=i+r,j+c
                if 0<=dr<m and 0<=dc<n and (dr,dc) not in seen and grid[dr][dc]=="1":
                    dfs(dr,dc)
        for i in range(m):
            for j in range(n):
                if (i,j) not in seen and grid[i][j]=="1":
                    res+=1
                    dfs(i,j)
        return res