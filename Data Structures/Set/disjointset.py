class DisjointSet:
    """
    Class representing a disjoint set data structure.
    Also known as the Union-Find algorithm.
    """
    parent = {}
 
    # stores the depth of trees
    rank = {}
    
    # Store max size disjoint set
    largest_ds = 0
    
    # perform MakeSet operation
    def make_set(self, element):
        # create a disjoint set from the given element
        self.parent[element] = element
        self.rank[element] = 1
 
    # Find the root of the set in which element `k` belongs
    def find(self, k):
        # if `k` is not the root
        if self.parent[k] != k:
            # path compression
            self.parent[k] = self.find(self.parent[k])
        return self.parent[k]
 
    # Perform Union of two subsets
    def union(self, a, b):
        # find the root of the sets in which elements `x` and `y` belongs
        x = self.find(a)
        y = self.find(b)
 
        # if `x` and `y` are present in the same set
        if x == y:
            return
 
        # Always attach a smaller depth tree under the root of the deeper tree.
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.rank[x] += self.rank[y]
            self.largest_ds = max(self.largest_ds, self.rank[x])
        elif self.rank[x] <= self.rank[y]:
            self.parent[x] = y
            self.rank[y] += self.rank[x]
            self.largest_ds = max(self.largest_ds, self.rank[y])