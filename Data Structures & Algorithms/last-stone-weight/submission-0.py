class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.maxHeap = [-x for x in stones]
        heapq.heapify(self.maxHeap)
        while len(self.maxHeap) > 1:
            s1 = -heapq.heappop(self.maxHeap)
            s2 = -heapq.heappop(self.maxHeap)
            stone = s1 - s2
            if stone:
                heapq.heappush(self.maxHeap, -stone)

        if not self.maxHeap:
            return 0
        else:
            return -self.maxHeap[0]