class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1,s2=0,0
        merged=[]
        while s1!=len(word1) and s2!=len(word2):
            merged.append(word1[s1])
            merged.append(word2[s2])
            s1+=1
            s2+=1
        while s1!=len(word1):
            merged.append(word1[s1])
            s1+=1
        
        while s2!=len(word2):
            merged.append(word2[s2])
            s2+=1
        return ''.join(merged)
        