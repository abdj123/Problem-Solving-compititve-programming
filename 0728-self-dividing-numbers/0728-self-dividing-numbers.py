class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for i in range(left,right+1):
            print(i)
            if(i<10):
                res.append(i)
            else:
                temp=str(i)
                addIt=True
                for j in temp:
                    
                    if(int(j)==0 or i%int(j)!=0):
                        addIt=False
                        break
                if(addIt):
                    
                    res.append(i)
        return res
            