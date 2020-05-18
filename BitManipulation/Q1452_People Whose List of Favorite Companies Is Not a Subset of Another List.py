
# 思路1: 将整个companies用bit进行编码, 但是前提条件是整个company set不能超过32
# 思路2: 用set的内置函数subset进行判断

class Solution:
    # 思路1
    # def peopleIndexes(self, favoriteCompanies):
    #     companies = list(set([c for f in favoriteCompanies for c in f]))
    #     N = len(favoriteCompanies)
    #     idxmap = {c:i for i,c in enumerate(companies)}
    #     codes = [0]*N
    #     res = []
    #     for i,company in enumerate(favoriteCompanies):
    #         code = 0
    #         for c in company:
    #             code |= (1<<idxmap[c])
    #         codes[i] = code
    #     for i in range(N):
    #         curcode = codes[i]
    #         flag = 0
    #         for j in range(N):
    #             if j!=i:
    #                 if (codes[j]|curcode)==codes[j]:
    #                     flag = 1
    #                     break
    #         if not flag: res.append(i)
    #     return res

    # 思路2
    def peopleIndexes(self, favoriteCompanies):
        favoriteCompanies = [set(f) for f in favoriteCompanies]
        N = len(favoriteCompanies)
        res = []
        for i in range(N):
            curset = favoriteCompanies[i]
            flag = 0
            for j in range(N):
                if j!=i:
                    if curset.issubset(favoriteCompanies[j]):
                        flag = 1
                        break
            if not flag: res.append(i)
        return res

a=Solution()
print(a.peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]))
print(a.peopleIndexes([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]))
print(a.peopleIndexes([["leetcode"],["google"],["facebook"],["amazon"]]))