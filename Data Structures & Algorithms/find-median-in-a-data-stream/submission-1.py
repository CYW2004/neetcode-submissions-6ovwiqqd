import heapq

class MedianFinder:
    def __init__(self):
        self.small = [] # max heap
        self.large = [] # min hesp

    def addNum(self, num: int) -> None:
        # Step 1: push into max-heap (small)
        heapq.heappush(self.small, -num)

        # Step 2: ensure ordering: max(small) <= min(large)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Step 3: balance sizes: small can have at most 1 more than large
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])  # odd count
        return (-self.small[0] + self.large[0]) / 2.0  # even count
