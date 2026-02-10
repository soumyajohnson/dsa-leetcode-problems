class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        dp=[[-1]*(n+1) for _ in range(m+1)]
        def func(i,j):
            if i==0 or j==0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if text1[i-1]==text2[j-1]:
                dp[i][j]=1+func(i-1,j-1)
            else:
                dp[i][j]=max(func(i-1,j), func(i,j-1))
            return dp[i][j]
        return func(m,n)