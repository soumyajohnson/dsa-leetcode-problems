class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev=""
        for c in s[::-1]:
            if c.isalpha() or c.isdigit():
                rev+=c.lower()
        print(rev)
        return rev==rev[::-1]