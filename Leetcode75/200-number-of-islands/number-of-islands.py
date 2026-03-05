class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='0':
                return
            grid[i][j]='0'
            for dr,dc in dirs:
                dfs(i+dr,j+dc)
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    res+=1
                    dfs(i,j)
        return res