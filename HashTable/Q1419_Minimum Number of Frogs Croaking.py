from collections import Counter

# 思路: 用HashTable记录当前各个青蛙的状态，key为当前的字母
# 每来一个字母，从table中取对应的对接字母进行状态转换
# 如果字母为最后一个k，代表当前青蛙任务完成，进入闲置状态，""的数量+1
# 每来一个c，如果没有闲置青蛙，需要添加一个("")，并转为'c'
# 如果最后青蛙数量和""的数量相等，则正好完成

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs):
        trans = {'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a'}
        memo = Counter()
        res = 0
        for c in croakOfFrogs:
            if c == 'c':
                if not memo['']:
                    res += 1
                else:
                    memo[''] -= 1
                memo['c'] += 1
            else:
                if not memo[trans[c]]:
                    return -1
                memo[trans[c]] -= 1
                if c == 'k':
                    memo[''] += 1
                else:
                    memo[c] += 1
        return res if memo[''] == res else -1

a=Solution()
print(a.minNumberOfFrogs("croakcroak"))
print(a.minNumberOfFrogs("crcoakroak"))
print(a.minNumberOfFrogs("croakcrook"))
print(a.minNumberOfFrogs("croakcroa"))
print(a.minNumberOfFrogs("ccrrooaakk"))