class Solution(object):
    def updateMatrix(self, mat):
        q=[]
        print(len(mat))
        ans = [[-1 for j in mat[0]] for i in mat]
        # print(v)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    q.append([i,j])
                    ans[i][j]=0
        #bfs
        m=len(mat)
        n=len(mat[0])
        def checkValid(i,j,m,n):
            if i<0 or j<0 or i>=m or j>=n:
                return False
            else:
                return True
                
        while q:
            i=q[0][0]  
            j=q[0][1]
            
#checking for its neighbours is it valid or not valid...
            if checkValid(i+1,j,m,n) and ans[i+1][j]==-1:
                q.append([i+1,j])
                ans[i+1][j]=ans[i][j]+1
                
            if checkValid(i,j+1,m,n) and ans[i][j+1]==-1:
                q.append([i,j+1])
                ans[i][j+1]=ans[i][j]+1
                
            if checkValid(i-1,j,m,n) and ans[i-1][j]==-1:
                q.append([i-1,j])
                ans[i-1][j]=ans[i][j]+1
                
            if checkValid(i,j-1,m,n) and ans[i][j-1]==-1:
                q.append([i,j-1])
                ans[i][j-1]=ans[i][j]+1
            q.pop(0)
        return ans
                
        
                
        
        
            

                    
        
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        