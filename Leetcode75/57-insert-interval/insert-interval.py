class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res=[]
        curr=newInterval
        for i in intervals:
            if curr[0]>i[1]:
                res.append(i)
            elif curr[1]<i[0]:
                res.append(curr)
                curr=i
            elif i[1]>=curr[0] or i[0]<=curr[1]:
                curr[0]=min(curr[0], i[0])
                curr[1]=max(curr[1],i[1])
        res.append(curr)
        return res