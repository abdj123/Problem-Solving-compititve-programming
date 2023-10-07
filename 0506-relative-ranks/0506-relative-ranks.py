class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score=[(-i,ind) for ind , i in enumerate(score)]
        heapq.heapify(score)
        a=["Gold Medal","Silver Medal","Bronze Medal"]
        ans=[0]*len(score)
        ind=4
        while score:
            _,b=heapq.heappop(score)
            if a:
                ans[b]=a.pop(0)
            else:
                ans[b]="{}".format(ind)
                ind+=1
        return ans

        
          
        