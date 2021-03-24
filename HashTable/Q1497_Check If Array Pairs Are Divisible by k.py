from collections import Counter

# 思路: 比较余数分布即可, 所有余数分布能够配对即能成功
# 如果x=0 或者 k-x=x, 需要和自己配对，确定当前freq的奇偶即可

class Solution:
    def canArrange(self, arr, k: int) -> bool:
        reminders = Counter(n % k for n in arr)
        for x in reminders.keys():
            if x == 0 or x == k - x:
                if reminders[x] & 1 != 0:
                    return False
            else:
                if reminders[x] != reminders[k - x]:
                    return False
        return True


a=Solution()
print(a.canArrange([3,8,17,2,5,6], 10))
print(a.canArrange([1,2,3,4,5,10,6,7,8,9], 5))
print(a.canArrange([1,2,3,4,5,6], 7))
print(a.canArrange([1,2,3,4,5,6], 10))
print(a.canArrange([-10,10], 2))
print(a.canArrange([-1,1,-2,2,-3,3,-4,4], 3))