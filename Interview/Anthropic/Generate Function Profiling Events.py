from typing import List, Optional

class Solution1:
    def stackEvents(self, samples: List[str]) -> List[str]:
        def collectRemainStacks(memo):
            ops = "end:" + time + ":"
            funcs = []
            while memo.keys():
                curFunc = list(memo.keys())[0]
                funcs.append(curFunc)
                memo = memo[curFunc]
            res.extend([ops + func for func in funcs[::-1]])

        root = {}
        res = []
        for sample in samples:
            time, stack = sample.split(':')
            funcs = [func for func in stack.split('->') if func]
            memo = root
            for func in funcs:
                if func in memo:
                    memo = memo[func]
                else:
                    if memo: 
                        collectRemainStacks(memo)
                        memo.clear()
                    memo[func] = {}
                    memo = memo[func]
                    ops = "start:" + time + ":"
                    res += [ops + func]
            if memo: 
                collectRemainStacks(memo)
                memo.clear()
        return res




