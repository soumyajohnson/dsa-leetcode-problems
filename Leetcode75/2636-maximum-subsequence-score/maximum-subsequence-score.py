class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total=0
        nums=[]
        heap=[]
        res=0
        for i in range(len(nums1)):
            nums.append((nums2[i], nums1[i]))
        nums.sort(reverse=True)

        for n2,n1 in nums:
            if len(heap)==k:                
                total-=heapq.heappop(heap)
            heapq.heappush(heap,n1)
            total+=n1
            if len(heap)==k:
                res=max(res,total*n2)
        return res