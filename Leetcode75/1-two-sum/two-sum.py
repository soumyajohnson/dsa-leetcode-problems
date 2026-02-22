class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        nummap={}
        for i in range(n):
            num=target-nums[i]
            if num in nummap:
                return [nummap[num],i]
            nummap[nums[i]]=i