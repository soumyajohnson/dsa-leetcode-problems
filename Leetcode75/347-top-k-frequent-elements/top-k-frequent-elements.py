class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        heap=[]
        for c,f in c.items():
            heap.append((f,c))
        heapq.heapify(heap)
        res=[]
        while len(heap)>k:
           heapq.heappop(heap)
        return [n for f,n in heap]