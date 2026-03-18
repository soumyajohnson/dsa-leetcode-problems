
from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned=set(banned)
        paragraph=re.sub('[^\w\s]',' ',paragraph)
        paragraph=paragraph.lower().split()
        freq=defaultdict(int)
        for p in paragraph:
            if p not in banned:
                freq[p]+=1
        return max(freq, key=freq.get)