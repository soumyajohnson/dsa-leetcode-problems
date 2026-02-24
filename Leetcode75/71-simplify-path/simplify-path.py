class Solution:
    def simplifyPath(self, path: str) -> str:
        pathlist=path.split('/')
        stack=[]
        for p in pathlist:
            if p=='' or p=='.':
                continue
            elif p=="..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/'+'/'.join(stack)  