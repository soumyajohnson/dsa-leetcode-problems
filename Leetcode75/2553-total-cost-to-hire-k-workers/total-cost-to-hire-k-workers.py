class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n=len(costs)
        cost=0
        l,r=0,n-1
        pq=[]
        for i in range(candidates):
            if l<=r:
                heapq.heappush(pq,(costs[l],l))
                l+=1
            if l<=r:
                heapq.heappush(pq,(costs[r],r))
                r-=1
        print(pq)
        for i in range(k):
            c,idx=heapq.heappop(pq)
            cost+=c
            if idx<l and l<=r:
                heapq.heappush(pq,(costs[l],l))
                l+=1
            elif idx>l and l<=r:
                heapq.heappush(pq,(costs[r],r))
                r-=1
        return cost