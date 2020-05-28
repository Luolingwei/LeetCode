
# 思路1: Two pointers一个一个check

# 思路2: 找到第一个不同的char, 对比剩下的string是否相同

class Solution:
    # def isOneEditDistance(self, s, t):
    #     def check(s1, s2, l1, l2):
    #         i, j, count = 0, 0, 0
    #         while i < l1 and j < l2:
    #             if s1[i] != s2[j]:
    #                 if count > 0: return False
    #                 i += 1
    #                 count += 1
    #                 continue
    #             i, j = i + 1, j + 1
    #         return True
    #
    #     m, n = len(s), len(t)
    #     if abs(m - n) > 1: return False
    #     if m == n:
    #         return sum(s[i] != t[i] for i in range(m)) == 1
    #     elif m >= n:
    #         return check(s, t, m, n)
    #     else:
    #         return check(t, s, n, m)

    def isOneEditDistance(self, s, t):
        m,n,i = len(s),len(t),0
        while i<min(m,n):
            if s[i]!=t[i]:
                break
            i+=1
        if i==m==n: return False
        return s[i+(m>=n):]==t[i+(n>=m):]


a=Solution()
print(a.isOneEditDistance("ab","acb"))
print(a.isOneEditDistance("cab","ad"))
print(a.isOneEditDistance("a",""))
print(a.isOneEditDistance("ab","abc"))
print(a.isOneEditDistance("",""))