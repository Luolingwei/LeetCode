from collections import defaultdict

# 思路: 对于每个id, dfs搜索此 id 已有的email所属的其他id (利用email2Id dict), 因为他们是同一个人
# visited数组记录已访问的id, emails set收集每次dfs中拿到的所有email

class Solution:
    def accountsMerge(self, accounts):
        email2Id = defaultdict(list)
        visited, res = [0] * len(accounts), []

        for i, account in enumerate(accounts):
            for email in account[1:]:
                email2Id[email].append(i)

        def dfs(i):
            if visited[i]: return
            visited[i] = 1
            for email in accounts[i][1:]:
                emails.add(email)
                for nextId in email2Id[email]:
                    dfs(nextId)

        for i in range(len(accounts)):
            if not visited[i]:
                emails = set()
                dfs(i)
                res.append([accounts[i][0]] + sorted(emails))

        return res


a=Solution()
print(a.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))
print(a.accountsMerge([["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]))