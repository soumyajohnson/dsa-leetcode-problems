class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isomap={}
        for i,c in enumerate(s):
            if c not in isomap:
                if t[i] in isomap.values():
                    return False
                isomap[c]=t[i]
            elif isomap[c]!=t[i]:
                return False
        return True
