class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        res=[[],[]]
        lostmap=defaultdict(int)
        for m in matches:
            lostmap[m[0]]+=0
            lostmap[m[1]]+=1
        for p,l in lostmap.items():
            if l==0:
                res[0].append(p)
            if l==1:
                res[1].append(p)
        res[0].sort()
        res[1].sort()
        return res