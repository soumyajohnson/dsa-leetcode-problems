class Solution:
    def maximumSwap(self, num: int) -> int:
        nums=list(str(num))
        last=defaultdict(int)
        for i,n in enumerate(nums):
            last[int(n)]=i
        for i in range(len(nums)):
            curr=int(nums[i])
            for d in range(9,curr,-1):
                if d in last and last[d]>i:
                    nums[i],nums[last[d]]=nums[last[d]],nums[i]
                    return int("".join(nums))
        return num