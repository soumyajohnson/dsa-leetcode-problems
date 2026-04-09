class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mins=[]
        for t in timePoints:
            h,m=t.split(':')
            mins.append(int(h)*60+int(m))
        mins.sort()
        res=float("inf")
        for i in range(1,len(mins)):
            res=min(res,mins[i]-mins[i-1])
        res=min(1440-mins[-1]+mins[0],res)
        return res