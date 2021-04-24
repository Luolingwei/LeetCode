class Solution:

    # "abcde", [0,1,1], [1,3,2], [0,2,3]
    def find(self, s, intervals):
        intervals.sort(key = lambda x: x[0])
        merged = []
        for start,end,label in intervals:
            if not merged or start>merged[-1][1]:
                merged.append([start, end, label])
            else:
                if label == merged[-1][2]:
                    merged[-1][1] = max(merged[-1][1], end)
                else:
                    if start == merged[-1][0]:
                        merged.pop()
                    else:
                        merged[-1][1] = start
                    merged.append([start,end,label])
        return merged

a=Solution()
print(a.find("abcde", [[0,1,1], [0,2,3], [1,3,2], [3,4,2], [4,6,4]]))