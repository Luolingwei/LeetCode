
# 思路1:
# 对于每个前缀，如果在所有排序好的字符串中插入，一定会插入在所有以它为前缀的string前面
# 如果后面不是以它为前缀的string，则一定不存在它的前缀string
# 思路2: 建立前缀树，每次从当前到达的节点开始往下搜索，搜集所有下层的word，排序并返回前三个最小的

import bisect
class Solution:
    # Solution 1 76 ms
    def suggestedProducts(self, products, searchWord):
        products.sort()
        res=[]
        curS=""
        for c in searchWord:
            curS+=c
            pos=bisect.bisect_left(products,curS)
            res.append([w for w in products[pos:pos+3] if w.startswith(curS)])
        return res

    # Solution 2 464 ms
    # def suggestedProducts(self, products, searchWord):
    #     root, res = {}, []
    #     for word in products:
    #         node = root
    #         for c in word:
    #             node = node.setdefault(c, {})
    #         if '$' in node:
    #             node['$'].append(word)
    #         else:
    #             node['$'] = [word]
    #
    #     def search(node):
    #         nodes, ans = [node], []
    #         while nodes:
    #             temp = []
    #             for node in nodes:
    #                 for key in node:
    #                     if key == '$':
    #                         ans += node['$']
    #                     else:
    #                         temp.append(node[key])
    #             nodes = temp
    #         return sorted(ans)[:3]
    #
    #     node = root
    #     for w in searchWord:
    #         if w in node:
    #             node = node[w]
    #             res.append(search(node))
    #         else:
    #             node = {}
    #             res.append([])
    #     return res


a=Solution()
print(a.suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"],"mouse"))
print(a.suggestedProducts(["havana"],"havana"))