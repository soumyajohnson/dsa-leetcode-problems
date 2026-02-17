class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        n=len(strs)
        first=strs[0]
        last=strs[n-1]
        res=""
        i=0
        while i<len(first) and i<len(last):
            if first[i]!=last[i]:
                return res
            res+=first[i]
            i+=1
        return res