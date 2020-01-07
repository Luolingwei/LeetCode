
# 思路: 最多需要的转账次数为账目不为0的人的个数-1，(整个账目和为0，一次bfs遍历解决)
# 每分一个0的group，总次数减1，所以找到最多的和为0的圈，bfs寻找，每次剔除最小的一个圈，ans-1

import collections
class Solution:
    def minTransfers(self, transactions):
        def split():
            q = collections.deque([([0], debt[0])])
            while q:
                curi,curs = q.popleft()
                if curs == 0:
                    debt[:]=[debt[i] for i in range(len(debt)) if i not in curi]
                    break
                for j in range(curi[-1] + 1, len(debt)):
                    q.append((curi + [j], curs + debt[j]))

        debt = collections.defaultdict(int)
        for i, j, n in transactions:
            debt[i] -= n
            debt[j] += n
        debt = list(filter(None, debt.values()))
        ans = len(debt)
        while debt:
            split()
            ans -= 1
        return ans

a=Solution()
print(a.minTransfers([[6, 0, 50],[1, 6, 40],[2, 6, 10],[6, 3, 40],[6, 4, 10],[5, 6, 25]]))