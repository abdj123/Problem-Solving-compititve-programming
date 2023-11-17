class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        res=[]
        i,j=0,len(nums)-1
        nums.sort()
        while(i<j):
            a=nums[j]+nums[i]
            res.append(a)
            i+=1
            j-=1
        return max(res)