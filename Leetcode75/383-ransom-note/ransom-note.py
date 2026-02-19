from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        chars=defaultdict(int)
        for m in magazine:
            chars[m]+=1
        for r in ransomNote:
            if r in chars and chars[r]>0:
                chars[r]-=1
            else:
                return False
        return True