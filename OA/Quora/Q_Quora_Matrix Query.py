class Solution:

    def __init__(self,matrix):
        self.m,self.n=len(matrix),len(matrix[0])
        self.rows,self.cols=[1]*self.m,[1]*self.n

    def query(self):
        i,j=0,0
        ansi,ansj=None,None
        while i<self.m:
            if self.rows[i]:
                ansi=i
                break
            i+=1
        while j<self.n:
            if self.cols[j]:
                ansj=j
                break
            j+=1
        return (ansi+1)*(ansj+1)


    def disrow(self,i):
        self.rows[i-1]=0

    def discol(self,j):
        self.cols[j-1]=0


a=Solution(matrix=[[1,2,3],[4,5,6],[7,8,9]])
print(a.query())
a.disrow(1)
print(a.query())
a.discol(1)
print(a.query())