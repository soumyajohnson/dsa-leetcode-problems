class TimeMap:

    def __init__(self):
        self.timemap=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        values=self.timemap[key]
        l=0
        h=len(values)-1
        res=""
        while l<=h:
            mid=(l+h)//2
            if values[mid][0]<=timestamp:
                res=values[mid][1]
                l=mid+1
            else:
                h=mid-1
        return res




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)