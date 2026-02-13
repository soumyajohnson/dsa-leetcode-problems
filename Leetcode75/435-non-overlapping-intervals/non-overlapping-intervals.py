class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intvl=sorted(intervals, key=lambda x: x[1])
        res=0
        last=float("-inf")
        for i in intvl:
            if last>i[0]:
                res+=1
            else:
                last=i[1]
        return res