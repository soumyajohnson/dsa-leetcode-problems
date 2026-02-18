class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        res=float("inf")
        l,r=0,0
        curr=0
        while r<len(nums):
            curr+=nums[r]
            while curr>=target:
                res=min(res,r-l+1)
                curr-=nums[l]
                l+=1
            r+=1
        return res