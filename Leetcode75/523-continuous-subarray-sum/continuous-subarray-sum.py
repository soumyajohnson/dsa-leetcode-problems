class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        presum=0
        presum_map=defaultdict(int)
        presum_map[0]=-1
        n=len(nums)
        for i in range(n):
            presum+=nums[i]
            r=presum%k
            if r in presum_map:
                if i-presum_map[r]>=2:
                    return True
            else:
                presum_map[r]=i
        return False
            