class Solution:

    def __init__(self,matrix):
        self.m,self.n=len(matrix),len(matrix[0])
        self.disrows=set()
        self.discols=set()
        self.row=self.col=0

    def query(self):
        return (self.row+1)*(self.col+1)

    def disrow(self,i):
        self.disrows.add(i-1)
        while self.row in self.disrows:
            self.row+=1

    def discol(self,j):
        self.discols.add(j-1)
        while self.col in self.discols:
            self.col+=1


a=Solution(matrix=[[1,2,3],[4,5,6],[7,8,9]])
print(a.query())
a.disrow(1)
print(a.query())
a.discol(1)
print(a.query())