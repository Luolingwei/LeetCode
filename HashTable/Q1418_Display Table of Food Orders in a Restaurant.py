from collections import defaultdict

# 思路: 用两层defaultdict统计即可, {table:food:number}

class Solution:
    def displayTable(self, orders):
        res = []
        memo = defaultdict(lambda: defaultdict(int))
        foods = set()
        tables = set()
        for _, table, food in orders:
            memo[table][food] += 1
            foods.add(food)
            tables.add(table)
        tables = sorted(tables, key=lambda x: int(x))
        header = ['Table'] + sorted(foods)
        res.append(header)
        for table in tables:
            row = [table]
            for i in range(1, len(header)):
                row.append(str(memo[table][header[i]]))
            res.append(row)
        return res

a=Solution()
print(a.displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))
