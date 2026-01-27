class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen=0
        l=0
        cnt=0
        for r in range(len(nums)):
            if nums[r]==0:
                cnt+=1
            while cnt>k:
                if nums[l]==0:
                    cnt-=1
                l+=1
            maxlen=max(maxlen, r-l+1)     
        return maxlen

