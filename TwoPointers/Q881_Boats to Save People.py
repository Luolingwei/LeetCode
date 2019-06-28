# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)

# 思路: 一个船只能装两个人，将重量从大到小排列，将大的和小的组合在一起，如果大+小>limit，那么大的只能独自一组.

class Solution:
    def numRescueBoats(self, people, limit):
        people.sort(reverse=True)
        i,j=0,len(people)-1
        while i<=j:
            if people[i]+people[j]<=limit:
                j-=1
            i+=1
        return i

a=Solution()
print(a.numRescueBoats([3,1,1],))