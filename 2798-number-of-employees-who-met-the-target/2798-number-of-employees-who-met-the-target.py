class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res=0
        hours.sort()
        for i in range(len(hours)):
            if(hours[i]>=target):
                res=len(hours[i:])
                break
        return res
        