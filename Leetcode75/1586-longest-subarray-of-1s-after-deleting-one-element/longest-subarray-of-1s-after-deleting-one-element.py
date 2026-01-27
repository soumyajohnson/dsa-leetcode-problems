class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums0=0
        l,r=0,0
        max1=0
        while r<len(nums):
            if nums[r]==1:
                r+=1
            else:
                if nums0<1:
                    r+=1
                    nums0+=1
                else:
                    while l<r and nums[l]==1:
                        l+=1
                    l+=1
                    nums0-=1
            max1=max(max1,r-l-1)
        return max1



