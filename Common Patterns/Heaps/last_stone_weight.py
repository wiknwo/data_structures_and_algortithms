# https://realpython.com/python-heapq-module/
# https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python
# https://leetcode.com/problems/last-stone-weight/
import heapq

class Solution:
    def lastStoneWeight(self, stones):
        flipstones = [stone * -1 for stone in stones] # Multiply values in list by -1 to get values ready for max heap
        heapq.heapify(flipstones) # Turn list into maxheap using heapq module
        while len(flipstones) > 1:
            x = heapq.heappop(flipstones) * -1
            y = heapq.heappop(flipstones) * -1
            if x == y: 
                continue
            elif x != y:
                heapq.heappush(flipstones, abs(y - x) * -1)
        return flipstones[0] * -1 if len(flipstones) == 1 else 0