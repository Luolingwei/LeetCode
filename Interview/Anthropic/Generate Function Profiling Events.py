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


class Solution2:
    def stackEvents(self, samples: List[str]) -> List[str]:
        stack = []
        res = []
        for sample in samples:
            time, trace = sample.split(':')
            funcs = [func for func in trace.split('->') if func]
            for i, func in enumerate(funcs):
                # func does not exist in stack
                if i >= len(stack):
                    res.append("start:" + time + ":" + func)
                # mismatch point, first end, then start
                elif stack[i] != func:
                    ops = "end:" + time + ":"
                    res += [ops + f for f in stack[i:][::-1]]
                    stack = stack[:i]
                    res.append("start:" + time + ":" + func)
            # finished scanning cur trace, left some func in stack
            if len(funcs) < len(stack):
                ops = "end:" + time + ":"
                res += [ops + f for f in stack[len(funcs):][::-1]]
            stack = funcs
        return res

