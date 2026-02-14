class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mstack=[]
        ans=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            
            while mstack and temperatures[mstack[-1]]<temp:
                idx=mstack.pop()
                ans[idx]=i-idx
            mstack.append(i)
        return ans
                
