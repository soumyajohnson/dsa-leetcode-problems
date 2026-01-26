class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        if k>n:
            return 0
        window_sum=sum(nums[:k])
        max_avg=window_sum/k
        for i in range(k,n):
            window_sum+=nums[i]-nums[i-k]
            window_avg=window_sum/k
            max_avg=max(max_avg,window_avg)
        return max_avg