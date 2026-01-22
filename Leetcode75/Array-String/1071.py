class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1,l2=len(str1),len(str2)
        l=min(l1,l2)
        while l>0:
            if l1%l==0 and l2%l==0:
                f1,f2=l1//l,l2//l
                if f1*str1[:l]==str1 and f2*str1[:l]==str2:
                    return str1[:l]
            l-=1
        return ""
    