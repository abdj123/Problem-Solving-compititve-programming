class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        for i,v in enumerate(nums):
            if(v%2==0):
                nums.insert(0,nums.pop(i))
        return nums
                
        