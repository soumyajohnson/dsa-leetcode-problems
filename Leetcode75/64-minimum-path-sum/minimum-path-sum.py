class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo={}
        m=len(grid)
        n=len(grid[0])
        def func(i,j):
            if i>=m or j>=n:
                return float("inf")
            if i==m-1 and j==n-1:
                return grid[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)]=grid[i][j]+min(func(i+1,j),func(i,j+1))
            return memo[(i,j)]
        return func(0,0)