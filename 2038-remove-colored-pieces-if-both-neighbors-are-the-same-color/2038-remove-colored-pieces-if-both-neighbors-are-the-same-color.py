class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a=b=0
        for i in range(len(colors)-2):
            temp=colors[i:i+3]
          
            if(temp[0]=="A" and temp[1]=="A" and temp[-1]=="A"):
                a+=1
            elif(temp[0]=="B" and temp[1]=="B" and temp[-1]=="B"):
                b+=1
        return a>b
            
        
        