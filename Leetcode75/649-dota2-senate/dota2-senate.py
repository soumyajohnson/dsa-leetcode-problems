class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n=len(senate)
        r,d=[],[]
        for i in range(len(senate)):
            if senate[i]=='R':
                r.append(i)
            elif senate[i]=='D':
                d.append(i)
        while r and d:
            r1=r.pop(0)
            d1=d.pop(0)
            if r1<d1:
                r.append(n+r1)
            else:
                d.append(n+d1)
        return "Radiant" if r else "Dire"
