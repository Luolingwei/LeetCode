from typing import List, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
import heapq

class SegmentNum:
    def __init__(self, value, segId, segIdx):
        self.value = value
        self.segId = segId
        self.segIdx = segIdx
    
    def __lt__(self, other):
        return self.value < other.value


class Solution:
    def multiThreadSort(self, nums: List[int], k: int) -> List[int]:
        def sort_seg(start, end):
            nums[start: end] = sorted(nums[start: end])

        seg_length = len(nums) // k
        # number of seg which has longer length (seg_length+1)
        num_long_seg = len(nums) % k 
        segIndexs = [[0,0] for _ in range(k)]

        with ThreadPoolExecutor(max_workers=8) as executor:
            curidx = 0
            curlength = seg_length+1
            futures = {}
            for i in range(k):
                if i >= num_long_seg: curlength -= 1
                segIndexs[i] = [curidx, curidx+curlength]
                futures[executor.submit(sort_seg, curidx, curidx+curlength)] = (curidx, curidx+curlength)
                curidx += curlength

            for future in as_completed(futures):
                pass

        hq = []
        res = []
        # Start the heap with 1st num of each segment
        for i in range(k):
            heapq.heappush(hq, SegmentNum(nums[segIndexs[i][0]], i, 0))
        while hq:
            segment = heapq.heappop(hq)
            res.append(segment.value)
            # next num in this segment
            nextIdx = segIndexs[segment.segId][0] + segment.segIdx + 1
            if nextIdx < segIndexs[segment.segId][1]:
                heapq.heappush(hq, SegmentNum(nums[nextIdx], segment.segId, segment.segIdx + 1))
        return res


def test1():
    solution = Solution()
    nums = [42, -17, 33, 8, -99, 56, 0, 23, -42, 71, 19, -5, 88, 64, -31, 15, 99, -8, 3, 50, -60, 77, 12, -23,
            45, 6, -71, 38, 91, -14]
    print(solution.multiThreadSort(nums, 10))

if __name__ == "__main__":
    test1()
