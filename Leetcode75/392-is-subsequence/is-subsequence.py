class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        js,it=0,0
        while js<len(s) and it<len(t):
            if s[js]==t[it]:
                js+=1
            it+=1
        return js==len(s)