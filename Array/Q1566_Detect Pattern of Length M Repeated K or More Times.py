
# 思路: 用pattern构造目标数组, 从前往后扫描，看是否有符合的数组

class Solution:
    def containsPattern(self, arr, m, k):
        i = 0
        while i <= len(arr) - m * k:
            p = arr[i:i + m]
            if p * k == arr[i:i + m * k]:
                return True
            i += 1
        return False


a=Solution()
print(a.containsPattern([1,2,4,4,4,4],1,3))
