class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo={}
        n=len(triangle)
        def func(i,j):
            if i==n-1:
                return triangle[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)]=triangle[i][j]+min(func(i+1,j),func(i+1,j+1))
            return memo[(i,j)]
        return func(0,0)