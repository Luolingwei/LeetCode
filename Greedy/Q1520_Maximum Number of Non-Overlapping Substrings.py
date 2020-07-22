
# 思路: 找出所有字母的lindex和rindex, 因为要包含所有位置的字母, 所以找到一个interval之后要扩展
# 每次遍历l,r之间的字符串, 对其范围进行扩展, 直到范围不再扩大为止
# 对所有合法的interval按结束时间排序, 求出最多的interval数量

class Solution:
    def maxNumOfSubstrings(self, s):
        idxMemo = {c:(s.index(c),s.rindex(c)) for c in set(s)}
        intervals = []
        for c in set(s):
            l,r = idxMemo[c][0],idxMemo[c][1]
            while True:
                tmpl, tmpr = l, r
                for inC in set(s[l:r+1]):
                    l = min(l,idxMemo[inC][0])
                    r = max(r,idxMemo[inC][1])
                if (l,r) == (tmpl, tmpr):
                    break
            intervals.append([l,r])

        intervals.sort(key=lambda x:x[1])
        end = -1
        res = []
        for i,j in intervals:
            if i>end:
                res.append(s[i:j+1])
                end = j
        return res


a=Solution()
print(a.maxNumOfSubstrings("adefaddaccc"))
print(a.maxNumOfSubstrings("cabcccbaa"))