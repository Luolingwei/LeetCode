class Solution:

    def replace(self, text_in, replacements):
        pos = 0
        res = []
        for index, before, after in replacements:
            res.append(text_in[pos:index])
            pos = index
            res.append(after)
            pos += len(before)
        res.append(text_in[pos:])
        return "".join(res)


a=Solution()
print(a.replace("const foo num;;;;", [[6,"foo", "fxx"], [10, "num", "nxx"]]))
print(a.replace("foo num;;;;", [[0,"foo", "fxx"], [4, "num", "nxx"]]))