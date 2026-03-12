class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxsum=float("-inf")
        minsum=float("inf")
        currmax=0
        currmin=0
        for n in nums:
            currmax=max(n,currmax+n)
            maxsum=max(maxsum,currmax)
            currmin=min(n,currmin+n)
            minsum=min(minsum,currmin)
        if maxsum<0:
            return maxsum
        return max(maxsum,sum(nums)-minsum)