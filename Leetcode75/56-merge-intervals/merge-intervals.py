class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[]
        curr=intervals[0]
        for i in range(1,len(intervals)):
            if curr[1]>=intervals[i][0]:
                curr[1]=max(curr[1],intervals[i][1])
            else:
                res.append(curr)
                curr=intervals[i]
        res.append(curr)
        return res