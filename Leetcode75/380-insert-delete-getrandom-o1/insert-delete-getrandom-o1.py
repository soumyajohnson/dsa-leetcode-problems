class RandomizedSet:

    def __init__(self):
        self.nums=defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.nums:
            return False
        self.nums[val]=val
        return True

    def remove(self, val: int) -> bool:
        if val in self.nums:
            del self.nums[val]
            return True
        return False

    def getRandom(self) -> int:
        values=list(self.nums.values())
        return random.choice(values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()