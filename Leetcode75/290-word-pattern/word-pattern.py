class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        if len(words)!=len(pattern):
            return False
        pmap={}
        wmap={}
        for w,p in zip(words,pattern):
            if p in pmap and pmap[p]!=w:
                return False
            if w in wmap and wmap[w]!=p:
                return False
            pmap[p]=w
            wmap[w]=p
        return True