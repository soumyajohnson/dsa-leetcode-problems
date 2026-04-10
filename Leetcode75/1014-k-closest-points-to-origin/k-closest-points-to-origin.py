import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n=len(points)
        dist=[]
        for p in points:
            d=math.sqrt(p[0]**2+p[1]**2)
            dist.append((d,p))
        heapq.heapify(dist)
        res=[]
        while k>0:
            res.append(heapq.heappop(dist)[1])
            k-=1
        return res