class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        dist={}
        for i in range(1,n+1):
            dist[i]=float("inf")
        dist[k]=0
        q=[(k,0)]
        while q:
            u,d=heapq.heappop(q)
            if d>dist[u]:
                continue
            for v,w in graph[u]:
                newd=d+w
                if newd<dist[v]:
                    dist[v]=newd
                    heapq.heappush(q,(v,newd))
        res=max(dist.values())
        return res if res!=float("inf") else -1