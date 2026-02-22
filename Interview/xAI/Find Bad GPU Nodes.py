from typing import List

# External API that checks if a version supports a specific feature.
# You should NOT directly access the `badNodes`.
class TestServer:
    def __init__(self, n: int, badList: List[int]):
        self.badNodes = [False] * n
        for idx in badList:
            self.badNodes[idx] = True
        self.callCount = 0

    def test(self, nodes: List[int]) -> bool:
        if len(nodes) < 2:
            raise ValueError("Each batch must contain at least two nodes.")
        self.callCount += 1
        for idx in nodes:
            if self.badNodes[idx]:
                return False
        return True

    def getCallCount(self) -> int:
        return self.callCount


class Solution:
    def __init__(self, server: TestServer):
        self.server = server
        self.badNodes = []

    def findGoodSeed(self, n):
        for i in range(n):
            for j in range(i+1, n):
                if self.server.test([i, j]): 
                    return [i, j]
        raise RuntimeError("No good pair found!")

    def findBadNodes(self, n: int) -> List[int]:
        # TODO: Implement findBadNodes logic.
        good_seed = self.findGoodSeed(n)
        good_candidate = good_seed[0]
        candidates = [i for i in range(n) if i not in good_seed]
        self.searchBadNodes(good_candidate, candidates, 0, len(candidates))
        return self.badNodes
    
    def searchBadNodes(self, good_candidate, candidates, start, end):
        if start == end: return
        nodes = [good_candidate]
        for i in range(start, end):
            nodes.append(candidates[i])
        
        # All good nodes
        if self.server.test(nodes):
            return
        
        # Contain bad node
        if end - start == 1:
            self.badNodes.append(candidates[start])
            return

        # Divede into 2 segments and continue to find
        mid = start + (end - start) // 2
        self.searchBadNodes(good_candidate, candidates, start, mid)
        self.searchBadNodes(good_candidate, candidates, mid, end)

def main():
    test1()
    test2()
    test3()
    test4()
    test5()


def test1():
    print("===== Test 1 =====")
    server = TestServer(4, [1, 3])
    solution = Solution(server)
    print(solution.findBadNodes(4))  # Expected: [1, 3]
    print("Total calls: " + str(server.getCallCount()))


def test2():
    print("\n===== Test 2 =====")
    server = TestServer(5, [2])
    solution = Solution(server)
    print(solution.findBadNodes(5))  # Expected: [2]
    print("Total calls: " + str(server.getCallCount()))


def test3():
    print("\n===== Test 3 =====")
    server = TestServer(2, [])
    solution = Solution(server)
    print(solution.findBadNodes(2))  # Expected: []
    print("Total calls: " + str(server.getCallCount()))


def test4():
    print("\n===== Test 4 =====")
    server = TestServer(20, [2, 5, 6, 11, 17])
    solution = Solution(server)
    print(solution.findBadNodes(20))  # Expected: [2, 5, 6, 11, 17]
    print("Total calls: " + str(server.getCallCount()))


def test5():
    print("\n===== Test 5 =====")
    server = TestServer(51, [0, 7, 25, 35, 49])
    solution = Solution(server)
    print(solution.findBadNodes(51))  # Expected: [0, 7, 25, 35, 49]
    print("Total calls: " + str(server.getCallCount()))


if __name__ == "__main__":
    main()
