from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainmap=defaultdict(int)
        for d in cpdomains:
            cpd=d.split(" ")
            cnt,dom=int(cpd[0]),cpd[1]
            domainmap[dom]+=cnt
            i=0
            while i<len(dom):
                if dom[i]=='.':
                    subdom=dom[i+1:len(dom)]
                    domainmap[subdom]+=cnt
                i+=1
        res=[]
        for dom,cnt in domainmap.items():
            res.append(f"{cnt} {dom}")
        return res