class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[-1]*len(word2) for _ in range(len(word1))]
        def func(i,j):
            if i==len(word1):
                return len(word2)-j
            if j==len(word2):
                return len(word1)-i
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i]==word2[j]:
                return func(i+1,j+1)
            dp[i][j]=1+min(func(i,j+1), func(i+1,j), func(i+1,j+1))
            return dp[i][j]
        return func(0,0)
