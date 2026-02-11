class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp=[[-1]*2 for _ in range(len(prices))]
        def func(i,canbuy):
            if i==len(prices):
                return 0
            if dp[i][canbuy]!=-1:
                return dp[i][canbuy]
            profit=0
            if canbuy:
                profit=max((-prices[i]+func(i+1,False)),func(i+1, True))
            else:
                profit=max((prices[i]-fee+func(i+1,True)),func(i+1, False))
            dp[i][canbuy]=profit
            return dp[i][canbuy]
        return func(0,True)
            