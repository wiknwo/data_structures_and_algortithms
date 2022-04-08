# https://leetcode.com/problems/kth-largest-element-in-a-stream/
# https://www.youtube.com/watch?v=q1f7Bwr3ajM
import heapq
class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.stream = []
        
        for num in nums:
            heapq.heappush(self.stream, num)
            
            if len(self.stream) > self.k:
                heapq.heappop(self.stream)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        
        if len(self.stream) > self.k:
                heapq.heappop(self.stream)
                
        return self.stream[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)