class Solution:
    def rob(self, nums: List[int]) -> int:
        dp={}
        def func(i):
            if i<0:
                return 0
            if i in dp:
                return dp[i]
            if i==0:
                return nums[0]
            rob=nums[i]+func(i-2)
            no_rob=func(i-1)
            dp[i]=max(rob,no_rob)
            return dp[i]
        return func(len(nums)-1)