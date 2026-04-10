class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum=0
        res=0
        presum_count=defaultdict(int)
        presum_count[0]=1
        for n in nums:
            presum+=n
            res+=presum_count[presum-k]
            presum_count[presum]+=1
        return res

