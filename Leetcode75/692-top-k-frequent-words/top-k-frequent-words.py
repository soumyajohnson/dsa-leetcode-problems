from collections import defaultdict
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq=defaultdict(int)
        for w in words:
            freq[w]+=1
        maxheap=[(-c,w) for w,c in freq.items()]
        heapq.heapify(maxheap)
        return [heapq.heappop(maxheap)[1] for _ in range (k)]