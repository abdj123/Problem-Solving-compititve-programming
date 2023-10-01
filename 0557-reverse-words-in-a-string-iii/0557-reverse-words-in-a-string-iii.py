class Solution:
    def reverseWords(self, s: str) -> str:
        temp=s.split()
        res=""
        
        for i in temp:
            res+=i[::-1]+" "
        return res[:-1]