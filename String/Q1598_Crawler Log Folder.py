
# 统计深度即可

class Solution:
    def minOperations(self, logs) -> int:
        depth = 0
        for log in logs:
            if log[:2] == ".." and depth>0:
                depth -= 1
            elif log[0] != ".":
                depth += 1
        return depth

a=Solution()
print(a.minOperations(["d1/","d2/","../","d21/","./"]))