class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nummap=defaultdict(int)
        for i,n in enumerate(nums):
            num=target-n
            if num in nummap:
                return [i,nummap[num]]
            nummap[n]=i
        