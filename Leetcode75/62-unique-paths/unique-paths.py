class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for _ in range(n)] for _ in range(m)]
        def func(x,y):
            if x==m-1 and y==n-1:
                return 1
            if dp[x][y]!=-1:
                return dp[x][y]
            down=0
            right=0
            if x<m-1:
                down=func(x+1,y)
            if y<n-1:
                right=func(x,y+1)
            dp[x][y]=down+right
            return dp[x][y]
        return func(0,0)