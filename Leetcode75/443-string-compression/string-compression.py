class Solution:
    def compress(self, chars: List[str]) -> int:
        i,j=0,0
        while i<len(chars):
            group=1
            while (i+group)<len(chars) and chars[i+group]==chars[i]:
                group+=1
            chars[j]=chars[i]
            j+=1
            if group>1:
                for g in str(group):
                    chars[j]=g
                    j+=1
            i+=group
        return j