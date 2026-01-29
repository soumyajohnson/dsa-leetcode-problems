class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for c in s:
            if c!=']':
                stack.append(c)
            else:
                substr=""
                while stack[-1]!='[':
                    substr=stack.pop()+substr
                stack.pop()
                n=""
                while stack and stack[-1].isdigit():
                    n=stack.pop()+n
                stack.append(int(n)*substr)
        return ''.join(stack)
