
# 思路: 类似Q1017 covert to base -2
# 为了防止reminder出现负数，每次reminder<0的时候，将reminder+2，carry+1,相当于少除了一个-2. 3/-2=-1余1 而不是 -2余-1

class Solution:
    def addNegabinary(self, arr1, arr2):
        ans,carry=[],0
        while arr1 or arr2 or carry:
            carry+=(arr1 or [0]).pop()+(arr2 or [0]).pop()
            carry,reminder=divmod(carry,-2)
            if reminder<0:
                carry,reminder=carry+1,reminder+2
            ans.append(reminder)
        while len(ans)>1 and ans[-1]==0:
            ans.pop()
        return ans[::-1]

a=Solution()
print(a.addNegabinary([1,1,1,1,1],[1,0,1]))
print(a.addNegabinary([1,1],[1,1]))
print(a.addNegabinary([1,0],[1,0]))
print(a.addNegabinary([0,0],[1,0,0]))
print(a.addNegabinary([1],[1,1]))