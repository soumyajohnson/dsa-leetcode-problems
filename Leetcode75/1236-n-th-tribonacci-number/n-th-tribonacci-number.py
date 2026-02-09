class Solution:
    def tribonacci(self, n: int) -> int:
        dp={}
        def func(i):
            if i in dp:
                return dp[i]
            if i==0:
                return 0
            elif i==1 or i==2:
                return 1
            else:
                dp[i]=func(i-1)+func(i-2)+func(i-3)
                return dp[i]
        return func(n)