class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        curr=newInterval
        res=[]
        for i in intervals:
            if i[1]<curr[0]:
                res.append(i)
            elif i[0]>curr[1]:
                res.append(curr)
                curr=i
            elif curr[0]<=i[1] or curr[1]>=i[0]:
                curr[0]=min(curr[0],i[0])
                curr[1]=max(curr[1],i[1])
        res.append(curr)
        return res
