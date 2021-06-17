from collections import defaultdict, deque

# 思路: 对每两个相邻的word建立字符的拓扑关系, 一旦两个同位置的字符不相等, 那么一定有cur_word[j] < next_word[j]
# after存储每个字符之后需要放的字符, {c: set(next_c1, next_c2...)}
# degree存储每个字符之前需要放的字符个数, 如果degree[c] == 0, 说明此字符已经可以随意放置, {c: n}
# 以degree[c] == 0 的 字符为起始集合, 对每个字符的 next_c减degree, degree == 0的再次加入q
# 最后检查是否所有字符都被纳入res

class Solution:
    def alienOrder(self, words):
        N = len(words)
        after = defaultdict(set)
        degree = defaultdict(int)
        for w in words:
            for c in w:
                degree[c] = 0

        for i in range(N - 1):
            cur_word = words[i]
            next_word = words[i + 1]
            L = min(len(cur_word), len(next_word))
            for j in range(L):
                if cur_word[j] != next_word[j]:
                    if next_word[j] not in after[cur_word[j]]:
                        after[cur_word[j]].add(next_word[j])
                        degree[next_word[j]] += 1
                    break
            # corner case, ["abc", "ab"]
            if cur_word[j] == next_word[j] and len(cur_word) > len(next_word): return ""

        q = deque([c for c in degree.keys() if degree[c] == 0])
        res = ""
        while q:
            c = q.popleft()
            res += c
            for next_c in after[c]:
                degree[next_c] -= 1
                if degree[next_c] == 0:
                    q.append(next_c)

        return res if len(res) == len(degree.keys()) else ""


a=Solution()
print(a.alienOrder(["wrt","wrf","er","ett","rftt"]))
print(a.alienOrder(["z","x"]))
print(a.alienOrder(["z","x","z"]))
print(a.alienOrder(["abc","ab"]))