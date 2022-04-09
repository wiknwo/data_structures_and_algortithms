# https://leetcode.com/problems/top-k-frequent-elements/
# https://docs.python.org/3/library/collections.html
# https://www.youtube.com/watch?v=Gj4-8sRi7W0
import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k: int):
        frequencies = Counter(nums) # Create dictionary mapping keys as numbers and values as the frequencies of the numbers
        frequencies = [(-v, k) for k, v in frequencies.items()] # Convert dictionary to list of -value, key pairs
        heapq.heapify(frequencies) # Convert the list into a max heap
        topkfreqelements = [] # Create a list to store the top k frequent elements
        for i in range(k):
            item = heapq.heappop(frequencies) # Pop a max (-value, key) tuple from the heap
            topkfreqelements.append(item[1]) # Add it to the top k frequent elements
        return topkfreqelements