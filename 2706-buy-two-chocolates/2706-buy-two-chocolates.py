class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        for i in range(1,len(prices)):
            tmp=prices[i]+prices[i-1]
            if(prices[i]<money and money-tmp>=0):
                return money-tmp
        return money
        
                
        