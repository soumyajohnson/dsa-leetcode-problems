class Solution:
    def romanToInt(self, s: str) -> int:
        num=0
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        for i in range(len(s)):
            if i+1<len(s) and roman_map[s[i]]<roman_map[s[i+1]]:
                num-=roman_map[s[i]]
            else:
                num+=roman_map[s[i]]
        return num
