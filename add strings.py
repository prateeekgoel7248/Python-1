class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1)<len(num2):
            return self.addStrings(num2,num1)
        n=len(num1)-1
        m=len(num2)-1
        num1=[i for i in num1]
        num2=[i for i in num2]
        flag=0
        while m>=0:
            temp= int(num1[n])+int(num2[m])+flag
            if temp>9:
                
                flag=1
            else:
                flag=0
            num1[n]=str(temp%10)
            
            n-=1
            m-=1
        # print(num1,flag)
        while flag and n>=0:
            temp=int(num1[n])+flag
            if temp>9:
                flag=1
            else:
                flag=0
            # print(n,temp%10)
            num1[n]=str(temp%10)
            n-=1
        
        if flag and n==-1:
                return '1'+''.join(num1)
           
        return ''.join(num1)
            
        
        