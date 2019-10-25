
# 思路:用一个数组放seats的下标，每次放入时遍历找到最大gap，leave时从数组中remove即可

import bisect
class ExamRoom:

    def __init__(self,N):
        self.N=N
        self.seats=[]

    def seat(self):
        res=0
        if self.seats:
            d=self.seats[0]
            for i in range(1,len(self.seats)):
                curd=(self.seats[i]-self.seats[i-1])//2
                if curd>d:
                    d=curd
                    res=curd+self.seats[i-1]
            if self.N-1-self.seats[-1]>d: res=self.N-1
        bisect.insort(self.seats,res)
        return res

    def leave(self, p):
        self.seats.remove(p)

a=ExamRoom(10)
print(a.seat())
print(a.seat())
print(a.seat())
print(a.seat())
a.leave(4)
print(a.seat())