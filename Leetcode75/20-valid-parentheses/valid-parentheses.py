class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={
            ")":"(",
            "]":"[",
            "}":"{"
        }
        for c in s:
            if c in '([{':
                stack.append(c)
            elif c in mapping:
                if not stack or mapping[c]!=stack.pop():
                    return False
        return len(stack)==0
