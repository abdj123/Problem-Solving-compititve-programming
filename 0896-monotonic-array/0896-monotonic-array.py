class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        temp=sorted(nums)
        return temp==nums or sorted(temp,reverse=True)==nums