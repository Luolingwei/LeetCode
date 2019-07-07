# Similar to Q1094 car pooling

# Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
# Output: [10,55,45,25,25]

# 思路: 对于booking的起止时间i,j，在第i天增加k个seat，在第j+1天减少k个seat, 得到各个时间点的changes，没有变化的时间点change为0
# 当前天的seat数量=前一天的seat数量+当前天的change

class Solution:
    def corpFlightBookings(self, bookings, n) :
        changes,ans=[0]*(n+2),[0]*(n+1)
        for i,j,seats in bookings:
            changes[i]+=seats
            changes[j+1]-=seats
        for i in range(1,n+1):
            ans[i]=ans[i-1]+changes[i]
        return ans[1:]

a=Solution()
print(a.corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]],5))