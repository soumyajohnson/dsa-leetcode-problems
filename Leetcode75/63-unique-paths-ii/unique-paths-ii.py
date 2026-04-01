class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo={}
        visited=set()
        m,n=len(obstacleGrid), len(obstacleGrid[0])
        def dfs(i,j):
            if i>=m or j>=n or obstacleGrid[i][j]==1:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)]=dfs(i+1,j)+dfs(i,j+1)
            return memo[(i,j)]
        return dfs(0,0)
            