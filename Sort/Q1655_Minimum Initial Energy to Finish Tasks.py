
# 思路: 先做minimal - actual大的task

class Solution:
    # 从前往后
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x:(x[0]-x[1]))
        res = energy = 0
        for cost,minE in tasks:
            res += max(0,minE-energy)
            energy = max(energy, minE)-cost
        return res

    # 从后往前
    def minimumEffort2(self, tasks):
        tasks.sort(key=lambda x:(x[1]-x[0]))
        res = 0
        for cost,minE in tasks:
            res = max(res+cost, minE)
        return res


a=Solution()
print(a.minimumEffort([[1,2],[2,4],[4,8]]))
print(a.minimumEffort([[1,3],[2,4],[10,11],[10,12],[8,9]]))
print(a.minimumEffort([[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]))
print(a.minimumEffort([[1,1],[1,3]]))