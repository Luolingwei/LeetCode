class Solution:
    '''
    use a bfs search to find minimum swap
    Note that each time only if the swap is valid we will swap, otherwise continue.
    And for each string, we only swap once and go further (break), as other positions could be swapped later.
    Use set() to remove duplications, improve efficiency.
    '''

    def kSimilarity(self, A: str, B: str):
        bfs = set()
        bfs.add(A)
        visited = {A}
        curswap = 0
        while bfs:
            new_bfs = set()
            if B in bfs:
                return curswap
            for curstr in bfs:
                for i in range(len(curstr)):
                    if B[i] == curstr[i]: continue
                    for j in range(i+1,len(curstr)):
                        if B[j] == curstr[i]:
                            newstr = curstr[:i] + curstr[j] + curstr[i+1:j] + curstr[i] + curstr[j+1:]
                            if newstr not in visited:
                                new_bfs.add(newstr)
                                visited.add(newstr)
                    break
            bfs = new_bfs
            curswap += 1
        return -1

a=Solution()
print(a.kSimilarity("ab","ba"))
print(a.kSimilarity("cdebcdeadedaaaebfbcf","baaddacfedebefdabecc"))