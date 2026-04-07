class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged=[]
        curr=intervals[0]
        for i in range(1, len(intervals)):
            if curr[1]>=intervals[i][0]:
                curr[1]=max(curr[1], intervals[i][1])
            else:
                merged.append(curr)
                curr=intervals[i]
        merged.append(curr)
        return merged
            