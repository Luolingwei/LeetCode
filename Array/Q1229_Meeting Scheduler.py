import bisect

# 思路1:
# 首先过滤掉小于duration的interval,因为他们不可能成为ans
# 将slots1和slots2按开始时间排序, 把slots2中的interval依次插入slots1中找到位置, 计算可能的gapl和gapr
# 如果出现符合的gap, 返回对应的范围即可
# O(max(nlogn,mlogm,nlogm))

# 思路2:
# 首先过滤掉小于duration的interval, 因为他们不可能成为ans
# 将slots1和slots2合并起来按开始时间排序
# 检查任意相邻两个interval的公共区间即可, 如果有交集, 一定是两个不同slots的
# O((m+n)log(m+n))

class Solution:
    # def minAvailableDuration(self, slots1, slots2, duration):
    #     slots1 = sorted([s for s in slots1 if s[1]-s[0]>=duration])
    #     slots2 = sorted([s for s in slots2 if s[1]-s[0]>=duration])
    #     m,n = len(slots1),len(slots2)
    #     for j in range(n):
    #         idx = bisect.bisect_left(slots1,slots2[j])
    #         gapl = min(slots1[idx-1][1],slots2[j][1])-slots2[j][0] if idx>0 else 0
    #         gapr = min(slots1[idx][1],slots2[j][1])-slots1[idx][0] if idx<m else 0
    #         if gapl>=duration:
    #             return [slots2[j][0],slots2[j][0]+duration]
    #         elif gapr>=duration:
    #             return [slots1[idx][0],slots1[idx][0]+duration]
    #     return []

    def minAvailableDuration(self, slots1, slots2, duration):
        s = sorted(list(filter(lambda s:s[1]-s[0]>=duration,slots1+slots2)))
        for i in range(len(s)-1):
            if s[i][1]>=s[i+1][0]+duration:
                return [s[i+1][0],s[i+1][0]+duration]
        return []


a=Solution()
print(a.minAvailableDuration([[10,50],[60,120],[140,210]],[[0,15],[60,70]],8))