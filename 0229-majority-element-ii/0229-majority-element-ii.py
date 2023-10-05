class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        for i in nums:
            if(i not in res and nums.count(i)>n/3):
                res.append(i)
        return res
        