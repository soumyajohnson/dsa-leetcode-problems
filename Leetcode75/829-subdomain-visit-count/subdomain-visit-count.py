class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dommap=defaultdict(int)
        for c in cpdomains:
            n,dom=c.split(" ")
            dommap[dom]+=int(n)
            while dom.find('.')!=-1:
                idx=dom.find('.')
                dom=dom[idx+1:]
                dommap[dom]+=int(n)
        res=[]
        for dom,n in dommap.items():
            res.append(f'{n} {dom}')
        return res
