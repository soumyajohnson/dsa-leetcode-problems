class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        fq1,fq2={},{}
        for w in word1:
            fq1[w]=fq1.get(w,0)+1
        for w in word2:
            fq2[w]=fq2.get(w,0)+1
        if set(fq1.keys())!=set(fq2.keys()):
            return False
        return sorted(fq1.values())==sorted(fq2.values())
