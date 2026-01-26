class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def count_vowel(s1:str)->int:
            v=0
            v+=s1.count('a')
            v+=s1.count('e')
            v+=s1.count('i')
            v+=s1.count('o')
            v+=s1.count('u')
            return v
        max_v=0
        for i in range(len(s)-k+1):
            sub_str=s[i:i+k]
            max_v=max(max_v,count_vowel(sub_str))
        return max_v