class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c=Counter(tasks)
        heap=[]
        for letter,freq in c.items():
            heapq.heappush(heap,-freq)
        max_freq=-(heapq.heappop(heap))
        max_freq_count=0
        for letter,freq in c.items():
            if freq==max_freq:
                max_freq_count+=1
        return max((n+1)*(max_freq-1)+max_freq_count,len(tasks))