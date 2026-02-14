class Solution:
    def numTilings(self, n: int) -> int:
        dp={}
        def func(i):
            if i==0:
                return 1
            if i==1:
                return 1
            if i==2:
                return 2
            if i in dp:
                return dp[i]
            dp[i]=2*func(i-1)+func(i-3)
            return dp[i]
        return func(n)%(10**9+7)