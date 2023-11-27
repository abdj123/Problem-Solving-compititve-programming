class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if(len(set(nums))==len(nums)):  #checking if duplicates exist.
            return(False)
        i=0
        while(i<len(nums)-1):
            if(len(set(nums[i:i+k+1]))!=len(nums[i:i+k+1])):
                return(True)
            i+=1
        return(False)
        