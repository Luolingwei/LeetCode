
# 思路1: 最多需要的转账次数为账目不为0的人的个数-1，(整个账目和为0，一次bfs遍历解决)
# 每分一个0的group，总次数减1，所以找到最多的和为0的圈，bfs寻找，每次剔除最小的一个圈，ans-1

# 思路2: 先将不为0的debt筛选出来, dfs搜索所有情况, 对于每个不为0的debt, 会转给一个另外的人
# 对于debts[i], dfs搜索i+1到末尾, 将他的debt转给任意一个人, 然后继续dfs搜索debts[i+1]
# 直到start到达数组末尾，说明所有debt已经settle完毕
# 优化细节是, debts[i]只转给跟他余额异号的人

from collections import defaultdict, deque
class Solution:

    # 思路1: 错误 X
    def minTransfers(self, transactions):
        def split():
            q = deque([([0], debt[0])])
            while q:
                curi,curs = q.popleft()
                if curs == 0:
                    print(curi)
                    debt[:]=[debt[i] for i in range(len(debt)) if i not in curi]
                    break
                for j in range(curi[-1] + 1, len(debt)):
                    q.append((curi + [j], curs + debt[j]))

        debt = defaultdict(int)
        for i, j, n in transactions:
            debt[i] -= n
            debt[j] += n
        debt = list(filter(None, debt.values()))
        print(debt)
        ans = len(debt)
        while debt:
            split()
            ans -= 1
        return ans


    # 思路2: 正确 ✔️
    def minTransfers2(self, transactions) -> int:
        def dfs(start, debts):
            while start < len(debts) and debts[start] == 0:
                start += 1
            if start == len(debts): return 0
            res = float('inf')
            for i in range(start + 1, len(debts)):
                if debts[i] * debts[start] < 0:
                    debts[i] += debts[start]
                    res = min(res, 1 + dfs(start + 1, debts))
                    debts[i] -= debts[start]
            return res

        debts = defaultdict(int)
        for x, y, amount in transactions:
            debts[x] -= amount
            debts[y] += amount

        debts = list(filter(None, debts.values()))
        return dfs(0, debts)


a=Solution()
print(a.minTransfers2([[6, 0, 50],[1, 6, 40],[2, 6, 10],[6, 3, 40],[6, 4, 10],[5, 6, 25]]))
print(a.minTransfers2([[1,0,18], [2,1,9], [4,3,11], [5,4,10], [5,6,7], [7,6,5], [8,7,3]]))