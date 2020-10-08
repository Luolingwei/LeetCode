from collections import defaultdict

# 思路: 用dic记录所有人之间继承关系, 需要getOrder时dfs遍历即可

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.memo = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.memo[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self):
        res = []

        def dfs(p):
            if p not in self.dead: res.append(p)
            for c in self.memo[p]:
                dfs(c)

        dfs("king")
        return res


t= ThroneInheritance("king")
t.birth("king", "andy")
t.birth("king", "bob")
t.birth("king", "catherine")
t.birth("andy", "matthew")
t.birth("bob", "alex")
t.birth("bob", "asha")
print(t.getInheritanceOrder()) # return ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
t.death("bob")
print(t.getInheritanceOrder()) # return ["king", "andy", "matthew", "alex", "asha", "catherine"]