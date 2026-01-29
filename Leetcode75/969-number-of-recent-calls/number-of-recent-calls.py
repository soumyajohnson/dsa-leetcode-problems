class RecentCounter:

    def __init__(self):
        self.requests=[]
        self.first=0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[self.first]< t-3000:
            self.first+=1
        return len(self.requests)-self.first

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)