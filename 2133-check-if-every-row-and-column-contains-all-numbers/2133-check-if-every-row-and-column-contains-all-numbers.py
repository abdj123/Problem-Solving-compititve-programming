class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        temp=[]
        for i in range(n):
            temp.append(i+1)
        for i in matrix:
            if(sorted(i)!=temp):
                return False
        for i in range(len(matrix)):
            t=[]
            for j in range(len(matrix)):
                t.append(matrix[j][i])
            if(sorted(t)!=temp):
                return False
        return True
            
                
        