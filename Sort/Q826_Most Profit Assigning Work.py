# Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
# Output: 100
# Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get profit of [20,20,30,30] seperately.

# 思路1: 按难度排序，找出每个人能cover难度的最大薪酬，累加，TLE
# 思路2: 改进，将worker也按ability排序，这样只需要遍历一遍jobs，因为jobs是按难度排序的. 中途记录每个人可以cover的最大薪酬即可.

class Solution:
    # Solution 1 bisect TLE
    # def maxProfitAssignment(self, difficulty, profit, worker):
    #     jobs,ans=sorted(zip(difficulty,profit)),0
    #     for w in worker:
    #         idx=bisect.bisect(jobs,(w,float('inf')))
    #         ans+=max([p for _,p in jobs[:idx]] or [0])
    #     return ans

    # Solution 2 120 ms
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs=sorted(zip(difficulty,profit))
        i,p,ans=0,0,0
        for w in sorted(worker):
            while i<len(jobs) and jobs[i][0]<=w:
                p=max(p,jobs[i][1])
                i+=1
            ans+=p
        return ans

a=Solution()
print(a.maxProfitAssignment([2,4,6,8,10],[10,20,30,40,50],[4,5,6,7]))
print(a.maxProfitAssignment([85,47,57],[24,66,99],[40,25,25]))