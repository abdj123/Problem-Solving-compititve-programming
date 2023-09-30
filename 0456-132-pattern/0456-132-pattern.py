class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # for i in range(len(nums)-2):
        #     temp=nums[i:i+3]
        #     if(temp[0]<temp[1 ]and temp[1]>temp[-1]):
        #         return True
        # return False
        
        stack,third=[],float('-inf')
        for num in reversed(nums):
            if num<third:
                return True
            while stack and stack[-1]<num:
                third=stack.pop()
            stack.append(num)
        return False
        