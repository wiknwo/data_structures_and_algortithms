# https://massivealgorithms.blogspot.com/2018/05/leetcode-692-top-k-frequent-words.html
# https://stackoverflow.com/questions/17930814/sorting-a-counter-in-python-by-keys
# https://stackoverflow.com/questions/64778567/top-k-frequent-words-using-heaps-in-python
# https://leetcode.com/problems/top-k-frequent-words/discuss/1928621/Python3-Two-line-solution-with-comments-Heap-O(nlogk)
import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, words, k: int):
        # Hash Table O(N) time
        frequencies = Counter(words)
        # Heap O(NlogK)
        # create lambda function that can sort by -freq and word order
        return heapq.nsmallest(k, frequencies, key=lambda word:(-frequencies[word], word))