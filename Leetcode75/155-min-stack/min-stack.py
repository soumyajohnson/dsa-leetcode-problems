class MinStack:

    def __init__(self):
        self.minele=[]
        self.stack=[]

    def push(self, val: int) -> None:
        if not self.minele:
            self.minele.append(val)
        elif val<=self.minele[-1]:
            self.minele.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        last=self.stack.pop()
        if last==self.minele[-1]:
            self.minele.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minele[-1]
        


# Your Minstack object will be instantiated and called as such:
# obj = Minstack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()