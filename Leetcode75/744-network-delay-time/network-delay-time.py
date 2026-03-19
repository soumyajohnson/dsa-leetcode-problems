from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        minheap=[(0,k)]
        time={i:float("inf") for i in range(1,n+1)}
        time[k]=0
        while minheap:
            curr,u=heapq.heappop(minheap)
            if curr>time[u]:
                continue
            for v,w in graph[u]:
                newtime=curr+w
                if newtime<time[v]:
                    time[v]=newtime
                    heapq.heappush(minheap,(newtime,v))
        res=max(time.values())
        return res if res!=float("inf") else -1
